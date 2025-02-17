
AVAILABLE_VARS = ["rmse", "bias", "quantiles", "mae", "gss", "fbias", "pod", "far", "sr", "csi", "stdev", "corr", "fss"]

AVAILABLE_LINE_TYPES = [
            "fho", "ctc", "cts", "cnt", "mctc", "mpr", "sl1l2", "sal1l2", 
            "vl1l2", "vcnt", "pct", "pstd", "pjc", "prc", "eclv", "sl1l2", 
            "sal1l2", "vl1l2", "val1l2", "vcnt", "mpr", "seeps_mpr", "seeps"
        ]

FULL_HEADER = [ 
    "version", "model", "desc", "fcst_lead", "fcst_valid_beg", "fcst_valid_end",
    "obs_lead", "obs_valid_beg", "obs_valid_end", "fcst_var", "fcst_units",
    "fcst_lev", "obs_var", "obs_units", "obs_lev", "obtype", "vx_mask",
    "interp_mthd", "interp_pnts", "fcst_thresh", "obs_thresh", "cov_thresh",
    "alpha", "line_type"
]

STATISTIC_TO_FIELDS1 = {
    'baser': ['fy_oy', 'fn_oy'],
    'acc': ['fy_oy', 'fn_on'],
    'fbias': ['fy_oy', 'fn_on', 'fn_oy', 'fy_on'],
    'fmean': ['fy_oy', 'fy_on'],
    'pody': ['fy_oy', 'fn_oy'],
    'pofd': ['fy_on', 'fn_on'],
    'podn': ['fn_on', 'fy_on'],
    'far': ['fy_on', 'fy_oy'],
    'csi': ['fy_oy', 'fy_on', 'fn_oy'],
    'gss': ['fy_oy', 'fy_on', 'fn_oy'],
    'hk': ['fy_oy', 'fn_oy', 'fy_on', 'fn_on'],
    'hss': ['fy_oy', 'fn_oy', 'fy_on', 'fn_on'],
    'odds': ['fy_oy', 'fn_oy', 'fy_on', 'fn_on'],
    'lodds': ['fy_oy', 'fn_oy', 'fy_on', 'fn_on'],
    'baggs': ['fy_oy', 'fn_oy', 'fy_on'],
    'eclv': ['fy_oy', 'fn_oy', 'fy_on', 'fn_on']
}

STATISTIC_TO_FIELDS2 = {
    'fbar': ['fbar'],
    'obar': ['obar'],
    'fstdev': ['fbar', 'ffbar'],
    'ostdev': ['obar', 'oobar'],
    'fobar': ['fobar'],
    'ffbar': ['ffbar'],
    'oobar': ['oobar'],
    'mae': ['mae'],
    'mbias': ['obar', 'fbar'],
    'corr': ['ffbar', 'fbar', 'oobar', 'obar', 'fobar'],
    'anom_corr': ['ffabar', 'fabar', 'ooabar', 'oabar', 'foabar'],
    'anom_corr_raw': ['ffabar', 'ooabar', 'foabar'],
    'rmsfa': ['ffabar'],
    'rmsoa': ['ooabar'],
    'me': ['fbar', 'obar'],
    'me2': ['fbar', 'obar'],
    'mse': ['ffbar', 'oobar', 'fobar'],
    'msess': ['ffbar', 'oobar', 'fobar', 'obar'],
    'rmse': ['ffbar', 'oobar', 'fobar'],
    'si': ['ffbar', 'oobar', 'fobar', 'obar'],
    'estdev': ['ffbar', 'oobar', 'fobar', 'fbar', 'obar'],
    'bcmse': ['ffbar', 'oobar', 'fobar', 'fbar', 'obar'],
    'bcrmse': ['ffbar', 'oobar', 'fobar', 'fbar', 'obar'],
    'pr_corr': ['ffbar', 'oobar', 'fobar', 'fbar', 'obar']
}

LINE_TYPE_COLUMNS = {
    "fho": ["total", "f_rate", "h_rate", "o_rate"],
    "ctc": ["total", "fy_oy", "fy_on", "fn_oy", "fn_on", "ec_value"],
    "cts": ["total", "baser", "baser_ncl", "baser_ncu", "baser_bcl", "baser_bcu",
            "fmean", "fmean_ncl", "fmean_ncu", "fmean_bcl", "fmean_bcu",
            "acc", "acc_ncl", "acc_ncu", "acc_bcl", "acc_bcu",
            "fbias", "fbias_bcl", "fbias_bcu",
            "pody", "pody_ncl", "pody_ncu", "pody_bcl", "pody_bcu",
            "podn", "podn_ncl", "podn_ncu", "podn_bcl", "podn_bcu",
            "pofd", "pofd_ncl", "pofd_ncu", "pofd_bcl", "pofd_bcu",
            "far", "far_ncl", "far_ncu", "far_bcl", "far_bcu",
            "csi", "csi_ncl", "csi_ncu", "csi_bcl", "csi_bcu",
            "gss", "gss_bcl", "gss_bcu",
            "hk", "hk_ncl", "hk_ncu", "hk_bcl", "hk_bcu",
            "hss", "hss_bcl", "hss_bcu",
            "odds", "odds_ncl", "odds_ncu", "odds_bcl", "odds_bcu",
            "lodds", "lodds_ncl", "lodds_ncu", "lodds_bcl", "lodds_bcu",
            "orss", "orss_ncl", "orss_ncu", "orss_bcl", "orss_bcu",
            "eds", "eds_ncl", "eds_ncu", "eds_bcl", "eds_bcu",
            "seds", "seds_ncl", "seds_ncu", "seds_bcl", "seds_bcu",
            "edi", "edi_ncl", "edi_ncu", "edi_bcl", "edi_bcu",
            "sedi", "sedi_ncl", "sedi_ncu", "sedi_bcl", "sedi_bcu",
            "bagss", "bagss_bcl", "bagss_bcu"],
    "cnt": ["total", "fbar", "fbar_ncl", "fbar_ncu", "fbar_bcl", "fbar_bcu",
            "fstdev", "fstdev_ncl", "fstdev_ncu", "fstdev_bcl", "fstdev_bcu",
            "obar", "obar_ncl", "obar_ncu", "obar_bcl", "obar_bcu",
            "ostdev", "ostdev_ncl", "ostdev_ncu", "ostdev_bcl", "ostdev_bcu",
            "pr_corr", "pr_corr_ncl", "pr_corr_ncu", "pr_corr_bcl", "pr_corr_bcu",
            "sp_corr", "kt_corr", "ranks", "frank_ties", "orank_ties",
            "me", "me_ncl", "me_ncu", "me_bcl", "me_bcu",
            "estdev", "estdev_ncl", "estdev_ncu", "estdev_bcl", "estdev_bcu",
            "mbias", "mbias_bcl", "mbias_bcu",
            "mae", "mae_bcl", "mae_bcu",
            "mse", "mse_bcl", "mse_bcu",
            "bcmse", "bcmse_bcl", "bcmse_bcu",
            "rmse", "rmse_bcl", "rmse_bcu"] +
            [f"e{p}" for p in ["10", "25", "50", "75", "90"]] +
            [f"e{p}_{x}" for p in ["10", "25", "50", "75", "90"] for x in ["bcl", "bcu"]] +
            ["eiqr", "eiqr_bcl", "eiqr_bcu",
             "mad", "mad_bcl", "mad_bcu",
             "anom_corr", "anom_corr_ncl", "anom_corr_ncu", "anom_corr_bcl", "anom_corr_bcu",
             "me2", "me2_bcl", "me2_bcu",
             "msess", "msess_bcl", "msess_bcu",
             "rmsfa", "rmsfa_bcl", "rmsfa_bcu",
             "rmsoa", "rmsoa_bcl", "rmsoa_bcu",
             "anom_corr_uncntr", "anom_corr_uncntr_bcl", "anom_corr_uncntr_bcu",
             "si", "si_bcl", "si_bcu"],
    "mctc": ["total", "n_cat"] + [f"fi_oj_{i}" for i in range(1, 100)] + ["ec_value"],
    "mpr": ["total", "index", "obs_sid", "obs_lat", "obs_lon", "obs_lvl", "obs_elv",
            "fcst", "obs", "obs_qc", "obs_climo_mean", "obs_climo_stdev", "obs_climo_cdf",
            "fcst_climo_mean", "fcst_climo_stdev"],
    "sl1l2": ["total", "fbar", "obar", "fobar", "ffbar", "oobar", "mae"],
    "sal1l2": ["total", "fabar", "oabar", "foabar", "ffabar", "ooabar", "mae"],
    "vl1l2": ["total", "ufbar", "vfbar", "uobar", "vobar", "uvfobar", "uvffbar",
              "uvoobar", "f_speed_bar", "o_speed_bar", "total_dir", "dir_me",
              "dir_mae", "dir_mse"],
    "vcnt": ["total", 
             "fbar", "fbar_bcl", "fbar_bcu",
             "obar", "obar_bcl", "obar_bcu",
             "fs_rms", "fs_rms_bcl", "fs_rms_bcu",
             "os_rms", "os_rms_bcl", "os_rms_bcu",
             "msve", "msve_bcl", "msve_bcu",
             "rmsve", "rmsve_bcl", "rmsve_bcu",
             "fstdev", "fstdev_bcl", "fstdev_bcu",
             "ostdev", "ostdev_bcl", "ostdev_bcu",
             "fdir", "fdir_bcl", "fdir_bcu",
             "odir", "odir_bcl", "odir_bcu",
             "fbar_speed", "fbar_speed_bcl", "fbar_speed_bcu",
             "obar_speed", "obar_speed_bcl", "obar_speed_bcu",
             "vdiff_speed", "vdiff_speed_bcl", "vdiff_speed_bcu",
             "vdiff_dir", "vdiff_dir_bcl", "vdiff_dir_bcu",
             "speed_err", "speed_err_bcl", "speed_err_bcu",
             "speed_abserr", "speed_abserr_bcl", "speed_abserr_bcu",
             "dir_err", "dir_err_bcl", "dir_err_bcu",
             "dir_abserr", "dir_abserr_bcl", "dir_abserr_bcu",
             "anom_corr", "anom_corr_ncl", "anom_corr_ncu", "anom_corr_bcl", "anom_corr_bcu",
             "anom_corr_uncntr", "anom_corr_uncntr_bcl", "anom_corr_uncntr_bcu",
             "total_dir",
             "dir_me", "dir_me_bcl", "dir_me_bcu",
             "dir_mae", "dir_mae_bcl", "dir_mae_bcu",
             "dir_mse", "dir_mse_bcl", "dir_mse_bcu",
             "dir_rmse", "dir_rmse_bcl", "dir_rmse_bcu"],
    "mcts": ["total", "n_cat",
             "acc", "acc_ncl", "acc_ncu", "acc_bcl", "acc_bcu",
             "hk", "hk_bcl", "hk_bcu",
             "hss", "hss_bcl", "hss_bcu",
             "ger", "ger_bcl", "ger_bcu",
             "hss_ec", "hss_ec_bcl", "hss_ec_bcu",
             "ec_value"],
    "pct": ["total", "n_thresh"] +
           [item for i in range(1, 100) for item in (f"thresh_{i}", f"oy_{i}", f"on_{i}")] +
           ["thresh_n"],
    "pstd": ["total", "n_thresh",
             "baser", "baser_ncl", "baser_ncu",
             "reliability", "resolution", "uncertainty",
             "roc_auc",
             "brier", "brier_ncl", "brier_ncu",
             "briercl", "briercl_ncl", "briercl_ncu",
             "bss", "bss_smpl"] +
            [f"thresh_{i}" for i in range(1, 100)] +
            ["thresh_n"],
    "pjc": ["total", "n_thresh"] +
           [item for i in range(1, 100) for item in (f"thresh_{i}", f"oy_tp_{i}", f"on_tp_{i}",
                                                     f"calibration_{i}", f"refinement_{i}", 
                                                     f"likelihood_{i}", f"baser_{i}")] +
           ["thresh_n"],
    "prc": ["total", "n_thresh"] +
           [item for i in range(1, 100) for item in (f"thresh_{i}", f"pody_{i}", f"pofd_{i}")] +
           ["thresh_n"],
    "eclv": ["total", "baser", "value_baser", "n_pnt"] +
            [f"cl_{i}" for i in range(1, 100)] +
            [f"value_{i}" for i in range(1, 100)],
    "val1l2": ["total",
               "ufabar", "vfabar",
               "uoabar", "voabar",
               "uvfoabar",
               "uvffabar",
               "uvooabar",
               "fa_speed_bar",
               "oa_speed_bar",
               "total_dir",
               "dira_me",
               "dira_mae",
               "dira_mse"],
    "seeps_mpr": ["obs_sid", "obs_lat", "obs_lon", "fcst", "obs", "obs_qc",
                  "fcst_cat", "obs_cat", "p1", "p2", "t1", "t2", "seeps"],
    "seeps": ["total",
              "odfl", "odfh", "olfd", "olfh", "ohfd", "ohfl",
              "pf1", "pf2", "pf3",
              "pv1", "pv2", "pv3",
              "seeps"]
}