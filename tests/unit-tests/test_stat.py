import os
import glob
import subprocess
import yaml
import unittest
import filecmp
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

class TestVcastStatConfigs(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Dynamically load all config_stat_*.yaml files, run vcast for each,
        and record the expected and control output file paths.
        """
        cls.test_cases = []
        # Discover all configuration files matching the pattern.
        config_files = glob.glob("configs/config_stat_*.yaml")
        logger.info(f"Found {len(config_files)} config_stat YAML files.")
        
        for config_file in config_files:
            logger.info(f"Processing config file: {config_file}")
            # Load the YAML configuration.
            with open(config_file, "r") as f:
                config_data = yaml.safe_load(f)
            # Determine output directory and filename from the YAML.
            output_dir = config_data.get("output_dir", ".")
            output_filename = config_data.get("output_filename", "stat-0001.data")
            expected_path = os.path.abspath(os.path.join(output_dir, output_filename))
            # Assume the corresponding control file is in control_outputs with the same name.
            control_path = os.path.abspath(os.path.join("control_outputs", output_filename))
            # Build a test case dictionary.
            test_case = {
                "config": config_file,
                "expected_files": [expected_path],
                "control_files": [control_path],
                "command": ["vcast", config_file]
            }
            cls.test_cases.append(test_case)

        # Run vcast for each config.
        for test_case in cls.test_cases:
            logger.info(f"Running command: {' '.join(test_case['command'])}")
            try:
                subprocess.run(
                    test_case["command"],
                    check=True,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
                logger.info(f"Command succeeded for {test_case['config']}")
            except subprocess.CalledProcessError as e:
                logger.error(f"vcast command failed for {test_case['config']}: {e}")
                raise RuntimeError(f"vcast command failed for {test_case['config']}: {e}")

    def test_files_exist(self):
        """
        Check that each expected output file is created.
        """
        for test_case in self.test_cases:
            for output_file in test_case["expected_files"]:
                with self.subTest(config=test_case["config"]):
                    logger.info(f"Checking existence of output file: {output_file}")
                    self.assertTrue(os.path.exists(output_file),
                                    f"Output file not found: {output_file}")

    def test_files_not_empty(self):
        """
        Check that each expected output file is not empty.
        """
        for test_case in self.test_cases:
            for output_file in test_case["expected_files"]:
                with self.subTest(config=test_case["config"]):
                    size = os.path.getsize(output_file)
                    logger.info(f"Output file {output_file} size: {size} bytes")
                    self.assertTrue(size > 0,
                                    f"Output file is empty: {output_file}")

    def test_output_matches_control_files(self):
        """
        Compare each generated output file with its corresponding control file.
        """
        for test_case in self.test_cases:
            if test_case["expected_files"] and test_case["control_files"]:
                for output_file, control_file in zip(test_case["expected_files"],
                                                     test_case["control_files"]):
                    with self.subTest(config=test_case["config"]):
                        logger.info(f"Comparing output file {output_file} with control file {control_file}")
                        self.assertTrue(os.path.exists(control_file),
                                        f"Control file not found: {control_file}")
                        # For image files, compare sizes; for others, do a full comparison.
                        if output_file.endswith(".png"):
                            output_size = os.path.getsize(output_file)
                            control_size = os.path.getsize(control_file)
                            logger.info(f"Image file sizes: output={output_size} bytes, control={control_size} bytes")
                            self.assertTrue(output_size == control_size,
                                            f"Image file {output_file} differs in size from control {control_file}.")
                        else:
                            identical = filecmp.cmp(output_file, control_file, shallow=False)
                            self.assertTrue(identical,
                                            f"Output file {output_file} does not match control file {control_file}")

    @classmethod
    def tearDownClass(cls):
        """
        Clean up: Delete the generated output files after tests.
        """
        for test_case in cls.test_cases:
            for output_file in test_case["expected_files"]:
                if os.path.exists(output_file):
                    try:
                        os.remove(output_file)
                        logger.info(f"Removed output file: {output_file}")
                    except Exception as e:
                        logger.error(f"Failed to remove {output_file}: {e}")

if __name__ == "__main__":
    unittest.main()
