"""
Personal Photometry Pipeline Configuation File
2016-11-01, mommermiscience@gmail.com

Telescopes setup for automated photometry
for
Astronomical Observatory Institute
Faculty of Physics
Adam Mickiewicz University in Poznań

modified: 2021-10-13 by EWil

2021-11-07 TK:   Added definition of PIT
                 Corrected definitions of RBT, UBC
               
2021-11-25 TK:   Corrected definition of PIT: shoud be flipped only
                 in x, not both in x and y, as it was before

2022-03-01 TK:   Added definition of PST1

2022-03-14 TK:   Added definition of DOAO (1.0-m in South Korea)
                 added definition of CAS (0.6-m Schmidt at Calar Alto)

2022-04-04 PKol: Added definition of ARO (0.33-m,  Abbey Ridge Observatory, Canada)
                 added definition of BGO (0.61-m, Burke-Gaffney Observatory, Canada)

2022-04-14 PKol: Added definition of 1-m telescope of Pic du Midi Observatory, France

2022-06-22 TK:   Added definition of 0.8-m IAC80 at Teide Observatory
                 CCD size refers to the cropped image, may not be valid for all images 

2022-07-04 PKol: Added definition of Remote Observatory Santa Maria de Montmagastrell, Tarrega, Spain 

           PKol: Added a "newRBT" entry that should be used for observations after filter replacement in October 2022.
                 Earlier observations should be processed with the old "RBT" entry.
                 PP treats frames with INSTRUME RBT as newRBT.
                 Frames with INSTRUME PST2/RBT entry use the old RBT entry.

2025-01-22 TK:   Added a "RBT2" entry that should be used for observations 
                 after 15 Nov 2024, when a focal reducer has been installed
                 PP treats frames with INSTRUME RBT2 as RBT2.


"""

# Photometry Pipeline
# Copyright (C) 2016-2018  Michael Mommert, mommermiscience@gmail.com

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see
# <http://www.gnu.org/licenses/>.

# telescope/instrument configurations

# MYTELESCOPE setup parameters
mytelescope_param = {
    'telescope_instrument': 'Telescope/Instrument',  # telescope/instrument name
    'telescope_keyword': 'mytelescope',  # telescope/instrument keyword
    'observatory_code': '695',  # MPC observatory code
    'secpix': (0.1, 0.1),  # pixel size (arcsec) before binning

    # image orientation preferences
    'flipx': True,
    'flipy': False,
    'rotate': 0,

    # instrument-specific FITS header keywords
    'binning': ('CCDBIN1', 'CCDBIN2'),  # binning in x/y
    'extent': ('NAXIS1', 'NAXIS2'),  # N_pixels in x/y
    'ra': 'RA',  # telescope pointing, RA
    'dec': 'DEC',  # telescope pointin, Dec
    'radec_separator': ':',  # RA/Dec hms separator, use 'XXX'
    # if already in degrees
    'date_keyword': 'DATE-OBS',  # obs date/time
    # keyword; use
    # 'date|time' if
    # separate
    'obsmidtime_jd': 'MJD-OBS',  # obs midtime jd keyword
    # (usually provided by
    # pp_prepare
    'object': 'OBJECT',  # object name keyword
    'filter': 'FILTER',  # filter keyword
    'filter_translations': {'g stuff': 'g'},
    # filtername translation dictionary
    'exptime': 'EXPTIME',  # exposure time keyword (s)
    'airmass': 'AIRMASS',  # airmass keyword

    # source extractor settings
    'source_minarea': 12,  # default sextractor source minimum N_pixels
    'source_snr': 3,  # default sextractor source snr for registration
    'aprad_default': 5,  # default aperture radius in px
    'aprad_range': [2, 10],  # [minimum, maximum] aperture radius (px)
    'sex-config-file': rootpath + '/setup/mytelescope.sex',
    'mask_file': {},
    #                        mask files as a function of x,y binning

    # scamp settings
    'scamp-config-file': rootpath + '/setup/mytelescope.scamp',
    'reg_max_mag': 19,
    'reg_search_radius': 0.5,  # deg
    'source_tolerance': 'high',
    
    # swarp settings
    'copy_keywords': ('OBSERVAT,INSTRUME,EXPTIME,OBJECT,' +
                      'DATE-OBS,TEL_KEYW'),
    #                        keywords to be copied in image
    #                        combination using swarp
    'swarp-config-file': rootpath+'/setup/mytelescope.swarp',

    # default catalog settings
    'astrometry_catalogs': ['GAIA'],
    'photometry_catalogs': ['PANSTARRS', 'SDSS-R9', 'APASS9', '2MASS']
}
# ------------------------------------------------------------------------------
lesedimkd_param = {
    'telescope_instrument': 'LESEDIMKD',  # telescope/instrument name
    'telescope_keyword': 'LESEDIMKD',  # telescope/instrument keyword
    'observatory_code': 'M28',  # MPC observatory code
    'secpix': (0.588 , 0.588),  # pixel size (arcsec) before binning

    # image orientation preferences
    'flipx': True,
    'flipy': False,
    'rotate': 0,

    # instrument-specific FITS header keywords
    'binning': ('HBIN', 'VBIN'),  # binning in x/y
    'extent': ('NAXIS1', 'NAXIS2'),  # N_pixels in x/y
    'ra': 'RA',  # telescope pointing, RA
    'dec': 'DEC',  # telescope pointin, Dec
    'radec_separator': ':',  # RA/Dec hms separator, use 'XXX'
    # if already in degrees
    'date_keyword': 'DATE-OBS',  # obs date/time
    # keyword; use
    # 'date|time' if
    # separate
    'obsmidtime_jd': 'MJD-OBS',  # obs midtime jd keyword
    # (usually provided by
    # pp_prepare
    'object': 'OBJECT',  # object name keyword
    'filter': 'FILTERA',  # filter keyword
    'filter_translations': {'out': 'G', 'u': 'u', 'g': 'g', 'r': 'r', 'i': 'i', 'z': 'z'},
    # filtername translation dictionary
    'exptime': 'EXPOSURE',  # exposure time keyword (s)
    'airmass': 'AIRMASS',  # airmass keyword

    # source extractor settings
    'source_minarea': 5,  # default sextractor source minimum N_pixels
    'source_snr': 3,  # default sextractor source snr for registration
    'aprad_default': 5,  # default aperture radius in px
    'aprad_range': [2, 10],  # [minimum, maximum] aperture radius (px)
    'sex-config-file': rootpath + '/setup/rbt.sex',
    'mask_file': {},
    #                        mask files as a function of x,y binning

    # scamp settings
    'scamp-config-file': rootpath + '/setup/rbt.scamp',
    'reg_max_mag': 19,
    'reg_search_radius': 0.5,  # deg
    'source_tolerance': 'high',

    # default catalog settings
    'astrometry_catalogs': ['GAIA'],
    'photometry_catalogs': ['SkyMapper', 'SDSS-R9', 'APASS9', 'PANSTARRS', '2MASS']
}
# add telescope configurations to 'official' telescopes.py
implemented_telescopes.append('LESEDIMKD')
# translate INSTRUME (or others, see _pp_conf.py) header keyword into PP telescope keyword
instrument_identifiers['LESEDIMKD'] = 'LESEDIMKD'
# translate telescope keyword into parameter set defined here
telescope_parameters['LESEDIMKD'] = lesedimkd_param

# ------------------------------------------------------------------------------
# KAO (Kottamia Astronomical Observatory, 1.88-m KFISP telescope)
kao_param = {
    'telescope_instrument': 'KFISP',  # telescope/instrument name
    'telescope_keyword': 'KFISP',  # telescope/instrument keyword
    'observatory_code': '88',  # MPC observatory code
    'secpix': (0.243, 0.243),  # pixel size (arcsec) before binning

    # image orientation preferences
    'flipx': False,
    'flipy': True,
    'rotate': 0,

    # instrument-specific FITS header keywords
    'binning': ('BINX', 'BINY'),  # binning in x/y
    'extent': ('NAXIS1', 'NAXIS2'),  # N_pixels in x/y
    'ra': 'RA',  # telescope pointing, RA
    'dec': 'DEC',  # telescope pointin, Dec
    'radec_separator': ':',  # RA/Dec hms separator, use 'XXX'
    # if already in degrees
    'date_keyword': 'DATETIME',  # obs date/time
    # keyword; use
    # 'date|time' if
    # separate
    'obsmidtime_jd': 'JD',  # obs midtime jd keyword
    # (usually provided by
    # pp_prepare
    'object': 'OBJECT',  # object name keyword
    'filter': 'FILTER',  # filter keyword
    'filter_translations': {'Empty': None, "SDSS-g'": 'g', "SDSS-r'": 'r', "SDSS-i'": 'i', "SDSS-z'": 'z'},
    # filtername translation dictionary
    'exptime': 'EXPTIME',  # exposure time keyword (s)
    'airmass': 'SEC_Z',  # airmass keyword

    # source extractor settings
    'source_minarea': 12,  # default sextractor source minimum N_pixels
    'source_snr': 3,  # default sextractor source snr for registration
    'aprad_default': 10,  # default aperture radius in px
    'aprad_range': [2, 15],  # [minimum, maximum] aperture radius (px)
    'sex-config-file': rootpath + '/setup/rbt.sex',
    'mask_file': {},
    #                        mask files as a function of x,y binning

    # scamp settings
    'scamp-config-file': rootpath + '/setup/rbt.scamp',
    'reg_max_mag': 19,
    'reg_search_radius': 0.5,  # deg
    'source_tolerance': 'high',
    
    # swarp settings
    'copy_keywords': ('OBJECT,EXPTIME,FILTER,DATE-BEG,UT,J_DATE'),
    #                        keywords to be copied in image
    #                        combination using swarp
    'swarp-config-file': rootpath+'/setup/rbt.swarp',

    # default catalog settings
    'astrometry_catalogs': ['GAIA'],
    'photometry_catalogs': ['PANSTARRS', 'SDSS-R9', 'APASS9', '2MASS']
}
# add telescope configurations to 'official' telescopes.py
implemented_telescopes.append('KFISP')
# translate INSTRUME (or others, see _pp_conf.py) header keyword into PP telescope keyword
instrument_identifiers['KFISP'] = 'KFISP'
# translate telescope keyword into parameter set defined here
telescope_parameters['KFISP'] = kao_param

# ------------------------------------------------------------------------------
# SAAO
saao_param = {
    'telescope_instrument': 'SAAO',  # telescope/instrument name
    'telescope_keyword': 'SAAO',  # telescope/instrument keyword
    'observatory_code': 'K95',  # MPC observatory code
    'secpix': (0.591, 0.591),  # pixel size (arcsec) before binning

    # image orientation preferences
    'flipx': False,
    'flipy': True,
    'rotate': 0,

    # instrument-specific FITS header keywords
    'binning': ('HBIN', 'VBIN'),  # binning in x/y
    'extent': ('NAXIS1', 'NAXIS2'),  # N_pixels in x/y
    'ra': 'RA',  # telescope pointing, RA
    'dec': 'DEC',  # telescope pointin, Dec
    'radec_separator': ':',  # RA/Dec hms separator, use 'XXX'
    # if already in degrees
    'date_keyword': 'DATE-OBS',  # obs date/time
    # keyword; use
    # 'date|time' if
    # separate
    'obsmidtime_jd': 'MJD',  # obs midtime jd keyword
    # (usually provided by
    # pp_prepare
    'object': 'OBJECT',  # object name keyword
    'filter': 'FILTERB',  # filter keyword
    'filter_translations': {'clear': 'R'},
    # filtername translation dictionary
    'exptime': 'EXPTIME',  # exposure time keyword (s)
    'airmass': 'AIRMASS',  # airmass keyword

    # source extractor settings
    'source_minarea': 12,  # default sextractor source minimum N_pixels
    'source_snr': 3,  # default sextractor source snr for registration
    'aprad_default': 10,  # default aperture radius in px
    'aprad_range': [2, 15],  # [minimum, maximum] aperture radius (px)
    'sex-config-file': rootpath + '/setup/rbt.sex',
    'mask_file': {},
    #                        mask files as a function of x,y binning

    # scamp settings
    'scamp-config-file': rootpath + '/setup/rbt.scamp',
    'reg_max_mag': 19,
    'reg_search_radius': 0.5,  # deg
    'source_tolerance': 'high',
    
    # swarp settings
    'copy_keywords': ('OBJECT,EXPTIME,FILTERB,DATE-BEG'),
    #                        keywords to be copied in image
    #                        combination using swarp
    'swarp-config-file': rootpath+'/setup/rbt.swarp',

    # default catalog settings
    'astrometry_catalogs': ['GAIA'],
    'photometry_catalogs': ['PANSTARRS', 'SDSS-R9', 'APASS9', '2MASS']
}
# add telescope configurations to 'official' telescopes.py
implemented_telescopes.append('SAAO')
# translate INSTRUME (or others, see _pp_conf.py) header keyword into PP telescope keyword
instrument_identifiers['SAAO'] = 'SAAO'
# translate telescope keyword into parameter set defined here
telescope_parameters['SAAO'] = saao_param


# ------------------------------------------------------------------------------

# RBT2 (RBT after installing focal reducer on 15 Nov 2024)
rbt2_param = {
    'telescope_instrument': 'RBT2',  # telescope/instrument name
    'telescope_keyword': 'RBT2',  # telescope/instrument keyword
    'observatory_code': '648',  # MPC observatory code
    'secpix': (0.828, 0.828),  # pixel size (arcsec) before binning

    # image orientation preferences
    'flipx': False,
    'flipy': True,
    'rotate': 0,

    # instrument-specific FITS header keywords
    'binning': ('HBIN', 'VBIN'),  # binning in x/y
    'extent': ('NAXIS1', 'NAXIS2'),  # N_pixels in x/y
    'ra': 'RA2000',  # telescope pointing, RA
    'dec': 'DEC2000',  # telescope pointin, Dec
    'radec_separator': 'XXX',  # RA/Dec hms separator, use 'XXX'
    # if already in degrees
    'date_keyword': 'DATE-BEG',  # obs date/time
    # keyword; use
    # 'date|time' if
    # separate
    'obsmidtime_jd': 'JD',  # obs midtime jd keyword
    # (usually provided by
    # pp_prepare
    'object': 'OBJNAME',  # object name keyword
    'filter': 'FILTER',  # filter keyword
    'filter_translations': {'0': 'L', '1': 'R', 
                            '2': 'g', '3': 'r',
                            '4': 'i', '5': 'z',
                            '6': None},
    # filtername translation dictionary
    'exptime': 'EXPOSURE',  # exposure time keyword (s)
    'airmass': 'AIRMASS',  # airmass keyword

    # source extractor settings
    'source_minarea': 12,  # default sextractor source minimum N_pixels
    'source_snr': 3,  # default sextractor source snr for registration
    'aprad_default': 10,  # default aperture radius in px
    'aprad_range': [2, 15],  # [minimum, maximum] aperture radius (px)
    'sex-config-file': rootpath + '/setup/rbt.sex',
    'mask_file': {},
    #                        mask files as a function of x,y binning

    # scamp settings
    'scamp-config-file': rootpath + '/setup/rbt.scamp',
    'reg_max_mag': 19,
    'reg_search_radius': 0.5,  # deg
    'source_tolerance': 'high',
    
    # swarp settings
    'copy_keywords': ('OBJNAME,EXPOSURE,FILTER,DATE,JD'),
    #                        keywords to be copied in image
    #                        combination using swarp
    'swarp-config-file': rootpath+'/setup/rbt.swarp',

    # default catalog settings
    'astrometry_catalogs': ['GAIA'],
    'photometry_catalogs': ['PANSTARRS', 'SDSS-R9', 'APASS9', '2MASS']
}
# add telescope configurations to 'official' telescopes.py
implemented_telescopes.append('RBT2')
# translate INSTRUME (or others, see _pp_conf.py) header keyword into PP telescope keyword
instrument_identifiers['RBT2'] = 'RBT2'
# translate telescope keyword into parameter set defined here
telescope_parameters['RBT2'] = rbt2_param

# ------------------------------------------------------------------------------


# newRBT (RBT after replacing filters in October 2022)
newrbt_param = {
    'telescope_instrument': 'RBT',  # telescope/instrument name
    'telescope_keyword': 'RBT',  # telescope/instrument keyword
    'observatory_code': '648',  # MPC observatory code
    'secpix': (0.579, 0.579),  # pixel size (arcsec) before binning

    # image orientation preferences
    'flipx': False,
    'flipy': True,
    'rotate': 0,

    # instrument-specific FITS header keywords
    'binning': ('HBIN', 'VBIN'),  # binning in x/y
    'extent': ('NAXIS1', 'NAXIS2'),  # N_pixels in x/y
    'ra': 'RA2000',  # telescope pointing, RA
    'dec': 'DEC2000',  # telescope pointin, Dec
    'radec_separator': 'XXX',  # RA/Dec hms separator, use 'XXX'
    # if already in degrees
    'date_keyword': 'DATE-BEG',  # obs date/time
    # keyword; use
    # 'date|time' if
    # separate
    'obsmidtime_jd': 'JD',  # obs midtime jd keyword
    # (usually provided by
    # pp_prepare
    'object': 'OBJNAME',  # object name keyword
    'filter': 'FILTER',  # filter keyword
    'filter_translations': {'0': 'L', '1': 'R', 
                            '2': 'g', '3': 'r',
                            '4': 'i', '5': 'z',
                            '6': None},
    # filtername translation dictionary
    'exptime': 'EXPOSURE',  # exposure time keyword (s)
    'airmass': 'AIRMASS',  # airmass keyword

    # source extractor settings
    'source_minarea': 12,  # default sextractor source minimum N_pixels
    'source_snr': 3,  # default sextractor source snr for registration
    'aprad_default': 10,  # default aperture radius in px
    'aprad_range': [2, 15],  # [minimum, maximum] aperture radius (px)
    'sex-config-file': rootpath + '/setup/rbt.sex',
    'mask_file': {},
    #                        mask files as a function of x,y binning

    # scamp settings
    'scamp-config-file': rootpath + '/setup/rbt.scamp',
    'reg_max_mag': 19,
    'reg_search_radius': 0.5,  # deg
    'source_tolerance': 'high',
    
    # swarp settings
    'copy_keywords': ('OBJNAME,EXPOSURE,FILTER,DATE,JD'),
    #                        keywords to be copied in image
    #                        combination using swarp
    'swarp-config-file': rootpath+'/setup/rbt.swarp',

    # default catalog settings
    'astrometry_catalogs': ['GAIA'],
    'photometry_catalogs': ['PANSTARRS', 'SDSS-R9', 'APASS9', '2MASS']
}
# add telescope configurations to 'official' telescopes.py
implemented_telescopes.append('RBT')
# translate INSTRUME (or others, see _pp_conf.py) header keyword into PP telescope keyword
instrument_identifiers['RBT'] = 'RBT'
# translate telescope keyword into parameter set defined here
telescope_parameters['RBT'] = newrbt_param

# ------------------------------------------------------------------------------

# RBT (before replacing filters in October 2022)
rbt_param = {
    'telescope_instrument': 'RBT/PST2',  # telescope/instrument name
    'telescope_keyword': 'RBT/PST2',  # telescope/instrument keyword
    'observatory_code': '648',  # MPC observatory code
    'secpix': (0.579, 0.579),  # pixel size (arcsec) before binning

    # image orientation preferences
    'flipx': False,
    'flipy': True,
    'rotate': 0,

    # instrument-specific FITS header keywords
    'binning': ('HBIN', 'VBIN'),  # binning in x/y
    'extent': ('NAXIS1', 'NAXIS2'),  # N_pixels in x/y
    'ra': 'RA2000',  # telescope pointing, RA
    'dec': 'DEC2000',  # telescope pointin, Dec
    'radec_separator': 'XXX',  # RA/Dec hms separator, use 'XXX'
    # if already in degrees
    'date_keyword': 'DATE-BEG',  # obs date/time
    # keyword; use
    # 'date|time' if
    # separate
    'obsmidtime_jd': 'JD',  # obs midtime jd keyword
    # (usually provided by
    # pp_prepare
    'object': 'OBJNAME',  # object name keyword
    'filter': 'FILTER',  # filter keyword
    'filter_translations': {'0': 'L', '1': 'U', 
                            '2': 'B', '3': 'V',
                            '4': 'R', '5': 'I',
                            '6': None},
    # filtername translation dictionary
    'exptime': 'EXPOSURE',  # exposure time keyword (s)
    'airmass': 'AIRMASS',  # airmass keyword

    # source extractor settings
    'source_minarea': 12,  # default sextractor source minimum N_pixels
    'source_snr': 3,  # default sextractor source snr for registration
    'aprad_default': 10,  # default aperture radius in px
    'aprad_range': [2, 15],  # [minimum, maximum] aperture radius (px)
    'sex-config-file': rootpath + '/setup/rbt.sex',
    'mask_file': {},
    #                        mask files as a function of x,y binning

    # scamp settings
    'scamp-config-file': rootpath + '/setup/rbt.scamp',
    'reg_max_mag': 19,
    'reg_search_radius': 0.5,  # deg
    'source_tolerance': 'high',
    
    # swarp settings
    'copy_keywords': ('OBJNAME,EXPOSURE,FILTER,DATE,JD'),
    #                        keywords to be copied in image
    #                        combination using swarp
    'swarp-config-file': rootpath+'/setup/rbt.swarp',

    # default catalog settings
    'astrometry_catalogs': ['GAIA'],
    'photometry_catalogs': ['PANSTARRS', 'SDSS-R9', 'APASS9', '2MASS']
}
# add telescope configurations to 'official' telescopes.py
implemented_telescopes.append('RBT/PST2')
# translate INSTRUME (or others, see _pp_conf.py) header keyword into PP telescope keyword
instrument_identifiers['RBT/PST2'] = 'RBT/PST2'
# translate telescope keyword into parameter set defined here
telescope_parameters['RBT/PST2'] = rbt_param

# ------------------------------------------------------------------------------

# UBC telescope
ubc_param = {
    'telescope_instrument': 'UBC',  # telescope/instrument name
    'telescope_keyword': 'UBC',  # telescope/instrument keyword
    'observatory_code': '695',  # MPC observatory code
    'secpix': (0.5156, 0.5156),  # pixel size (arcsec) before binning

    # image orientation preferences
    'flipx': False,
    'flipy': True,
    'rotate': 0,

    # instrument-specific FITS header keywords
    'binning': ('XBIN', 'YBIN'),  # binning in x/y
    'extent': ('NAXIS1', 'NAXIS2'),  # N_pixels in x/y
    'ra': 'RA',  # telescope pointing, RA
    'dec': 'DEC',  # telescope pointin, Dec
    'radec_separator': 'XXX',  # RA/Dec hms separator, use 'XXX'
    # if already in degrees
    'date_keyword': 'DATE-OBS',  # obs date/time
    # keyword; use
    # 'date|time' if
    # separate
    'obsmidtime_jd': 'MJD-OBS',  # obs midtime jd keyword
    # (usually provided by
    # pp_prepare
    'object': 'OBJECT',  # object name keyword
    'filter': 'FILTER',  # filter keyword
    'filter_translations': {'B': 'B', 'V': 'V', 'R': 'R', 'I': 'I'},
    # filtername translation dictionary
    'exptime': 'EXPTIME',# exposure time keyword (s)
    'airmass': 'TCSAM',  # airmass keyword

    # source extractor settings
    'source_minarea': 12,  # default sextractor source minimum N_pixels
    'source_snr': 3,  # default sextractor source snr for registration
    'aprad_default': 5,  # default aperture radius in px
    'aprad_range': [2, 10],  # [minimum, maximum] aperture radius (px)
    'sex-config-file': rootpath + '/setup/ubc.sex',
    'mask_file': {},
    #                        mask files as a function of x,y binning

    # scamp settings
    'scamp-config-file': rootpath + '/setup/ubc.scamp',
    'reg_max_mag': 19,
    'reg_search_radius': 0.5,  # deg
    'source_tolerance': 'high',
    
    # swarp settings
    'copy_keywords': ('OBSERVAT,INSTRUME,EXPTIME,OBJECT,' +
                      'DATE-OBS,TEL_KEYW'),
    #                        keywords to be copied in image
    #                        combination using swarp
    'swarp-config-file': rootpath+'/setup/ubc.swarp',

    # default catalog settings
    'astrometry_catalogs': ['GAIA'],
    'photometry_catalogs': ['PANSTARRS', 'SDSS-R9', 'APASS9', '2MASS']
}
# add telescope configurations to 'official' telescopes.py
implemented_telescopes.append('UBC')
# translate INSTRUME (or others, see _pp_conf.py) header keyword into PP telescope keyword
instrument_identifiers['UBC'] = 'UBC'
# translate telescope keyword into parameter set defined here
telescope_parameters['UBC'] = ubc_param

# ------------------------------------------------------------------------------

# GaiaGOSA Einari setup parameters
einari_param = {
    'telescope_instrument': 'Einari/Atik',  # telescope/instrument name
    'telescope_keyword': 'Einari/Atik',  # telescope/instrument keyword
    'observatory_code': '',  # MPC observatory code
    # 'secpix': (4.55, 4.55),  # pixel size (arcsec) before binning
    'secpix': (2.25, 2.25),  # pixel size (arcsec) before binning

    # image orientation preferences
    'flipx': False,
    'flipy': False,
    'rotate': 87.3,

    # instrument-specific FITS header keywords
    'binning': ('XBINNING', 'YBINNING'),  # binning in x/y
    'extent': ('NAXIS1', 'NAXIS2'),  # N_pixels in x/y
    'ra': 'CRVAL1',  # telescope pointing, RA
    'dec': 'CRVAL2',  # telescope pointin, Dec
    'radec_separator': 'XXX',  # RA/Dec hms separator, use 'XXX'
    # if already in degrees
    'date_keyword': 'DATE-OBS',  # obs date/time
    # keyword; use
    # 'date|time' if
    # separate
    'obsmidtime_jd': 'MJD-OBS',  # obs midtime jd keyword
    # (usually provided by
    # pp_prepare
    'object': 'OBJECT',  # object name keyword
    'filter': 'FILTER',  # filter keyword
    'filter_translations': {'G': None},
    # filtername translation dictionary
    'exptime': 'EXPOSURE',  # exposure time keyword (s)
    'airmass': 'AIRMASS',  # airmass keyword

    # source extractor settings
    'source_minarea': 12,  # default sextractor source minimum N_pixels
    'source_snr': 3,  # default sextractor source snr for registration
    'aprad_default': 5,  # default aperture radius in px
    'aprad_range': [2, 10],  # [minimum, maximum] aperture radius (px)
    'sex-config-file': rootpath + '/setup/einari.sex',
    'mask_file': {},
    #                        mask files as a function of x,y binning

    # scamp settings
    'scamp-config-file': rootpath + '/setup/einari.scamp',
    'reg_max_mag': 19,
    'reg_search_radius': 0.5,  # deg
    'source_tolerance': 'high',

    # swarp settings
    'copy_keywords': ('OBSERVAT,INSTRUME,EXPOSURE,OBJECT,' +
                      'DATE-OBS,TEL_KEYW'),
    #                        keywords to be copied in image
    #                        combination using swarp
    'swarp-config-file': rootpath + '/setup/einari.swarp',

    # default catalog settings
    'astrometry_catalogs': ['GAIA'],
    'photometry_catalogs': ['PANSTARRS', 'SDSS-R9', 'APASS9', '2MASS']
}
# add telescope configurations to 'official' telescopes.py
implemented_telescopes.append('Einari/Atik')
# translate INSTRUME (or others, see _pp_conf.py) header keyword into PP telescope keyword
instrument_identifiers['Atik Camera'] = 'Einari/Atik'
# translate telescope keyword into parameter set defined here
telescope_parameters['Einari/Atik'] = einari_param

#-----------------------------------------------------------------------------
# PIT: 0.4-m Poznań Imaging Telescope at Borowiec
pit_param = {
    'telescope_instrument': 'PIT',  # telescope/instrument name
    'telescope_keyword': 'PIT',  # telescope/instrument keyword
    'observatory_code': '187',   # MPC observatory code
    'secpix': (1.031, 1.031),    # pixel size (arcsec) before binning

    # image orientation preferences
    'flipx': True,
    'flipy': False,
    'rotate': 0,

    # instrument-specific FITS header keywords
    'binning': (1, 1),  # binning in x/y
    'extent': ('NAXIS1', 'NAXIS2'),  # N_pixels in x/y
    'ra': 'RA',  # telescope pointing, RA
    'dec': 'DEC',  # telescope pointin, Dec
    'radec_separator': 'XXX',  # RA/Dec hms separator, use 'XXX'
    # if already in degrees
    'date_keyword': 'DATE-OBS',  # obs date/time
    # keyword; use
    # 'date|time' if
    # separate
    'obsmidtime_jd': 'JD',  # obs midtime jd keyword
    # (usually provided by
    # pp_prepare
    'object': 'OBJECT',  # object name keyword
    'filter': 'FILTER',  # filter keyword
    'filter_translations': {'B': 'B', 'V': 'V',
                            'R': 'R', 'I': 'I',
                            'C': 'R'},
    # filtername translation dictionary
    'exptime': 'EXPTIME',  # exposure time keyword (s)
    'airmass': 'AIRMASS',  # airmass keyword

    # source extractor settings
    'source_minarea': 12,  # default sextractor source minimum N_pixels
    'source_snr': 3,  # default sextractor source snr for registration
    'aprad_default': 10,  # default aperture radius in px
    'aprad_range': [2, 15],  # [minimum, maximum] aperture radius (px)
    'sex-config-file': rootpath + '/setup/rbt.sex',
    'mask_file': {},
    #                        mask files as a function of x,y binning

    # scamp settings
    'scamp-config-file': rootpath + '/setup/rbt.scamp',
    'reg_max_mag': 19,
    'reg_search_radius': 0.5,  # deg
    'source_tolerance': 'high',
    
    # swarp settings
    'copy_keywords': ('OBJNAME,EXPOSURE,FILTER,DATE,JD'),
    #                        keywords to be copied in image
    #                        combination using swarp
    'swarp-config-file': rootpath+'/setup/rbt.swarp',

    # default catalog settings
    'astrometry_catalogs': ['GAIA'],
    'photometry_catalogs': ['PANSTARRS', 'SDSS-R9', 'APASS9', '2MASS']
}
# add telescope configurations to 'official' telescopes.py
implemented_telescopes.append('PIT')
# translate INSTRUME (or others, see _pp_conf.py) header keyword into PP telescope keyword
instrument_identifiers['PIT'] = 'PIT'
# translate telescope keyword into parameter set defined here
telescope_parameters['PIT'] = pit_param

#-----------------------------------------------------------------------------
# PST1: 0.5-m Poznań Spectroscopic Telescope No. 1
pst1_param = {
    'telescope_instrument': 'PST1',  # telescope/instrument name
    'telescope_keyword': 'PST1',  # telescope/instrument keyword
    'observatory_code': '187',   # MPC observatory code
    'secpix': (0.83, 0.83),    # pixel size (arcsec) before binning

    # image orientation preferences
    'flipx': True,
    'flipy': False,
    'rotate': 0,

    # instrument-specific FITS header keywords
    'binning': (1, 1),  # binning in x/y
    'extent': ('NAXIS1', 'NAXIS2'),  # N_pixels in x/y
    'ra': 'RA',  # telescope pointing, RA
    'dec': 'DEC',  # telescope pointin, Dec
    'radec_separator': 'XXX',  # RA/Dec hms separator, use 'XXX'
    # if already in degrees
    'date_keyword': 'DATE-OBS',  # obs date/time
    # keyword; use
    # 'date|time' if
    # separate
    'obsmidtime_jd': 'JD',  # obs midtime jd keyword
    # (usually provided by
    # pp_prepare
    'object': 'OBJECT',  # object name keyword
    'filter': 'FILTER',  # filter keyword
    'filter_translations': {'B': 'B', 'V': 'V',
                            'R': 'R', 'I': 'I',
                            'C': 'R'},
    # filtername translation dictionary
    'exptime': 'EXPTIME',  # exposure time keyword (s)
    'airmass': 'AIRMASS',  # airmass keyword

    # source extractor settings
    'source_minarea': 12,  # default sextractor source minimum N_pixels
    'source_snr': 3,  # default sextractor source snr for registration
    'aprad_default': 10,  # default aperture radius in px
    'aprad_range': [2, 15],  # [minimum, maximum] aperture radius (px)
    'sex-config-file': rootpath + '/setup/rbt.sex',
    'mask_file': {},
    #                        mask files as a function of x,y binning

    # scamp settings
    'scamp-config-file': rootpath + '/setup/rbt.scamp',
    'reg_max_mag': 19,
    'reg_search_radius': 0.5,  # deg
    'source_tolerance': 'high',
    
    # swarp settings
    'copy_keywords': ('OBJNAME,EXPOSURE,FILTER,DATE,JD'),
    #                        keywords to be copied in image
    #                        combination using swarp
    'swarp-config-file': rootpath+'/setup/rbt.swarp',

    # default catalog settings
    'astrometry_catalogs': ['GAIA'],
    'photometry_catalogs': ['PANSTARRS', 'SDSS-R9', 'APASS9', '2MASS']
}
# add telescope configurations to 'official' telescopes.py
implemented_telescopes.append('PST1')
# translate INSTRUME (or others, see _pp_conf.py) header keyword into PP telescope keyword
instrument_identifiers['PST1'] = 'PST1'
# translate telescope keyword into parameter set defined here
telescope_parameters['PST1'] = pst1_param

#-----------------------------------------------------------------------------
# PST1 0.5-m Poznań Spectroscopic Telescope No. 1
pst1_v2_param = {
    'telescope_instrument': 'PST1 SBIG ST7',  # telescope/instrument name
    'telescope_keyword': 'SBIG ST-7',  # telescope/instrument keyword
    'observatory_code': '187',   # MPC observatory code
    'secpix': (0.83, 0.83),    # pixel size (arcsec) before binning

    # image orientation preferences
    'flipx': True,
    'flipy': False,
    'rotate': 0,

    # instrument-specific FITS header keywords
    'binning': (1,1),  # binning in x/y
    'extent': ('NAXIS1', 'NAXIS2'),  # N_pixels in x/y
    'ra': 'CRVAL1',  # telescope pointing, RA
    'dec': 'CRVAL2',  # telescope pointin, Dec
    'radec_separator': 'XXX',  # RA/Dec hms separator, use 'XXX'
    # if already in degrees
    'date_keyword': 'DATE-OBS',  # obs date/time
    # keyword; use
    # 'date|time' if
    # separate
    'obsmidtime_jd': 'JD',  # obs midtime jd keyword
    # (usually provided by
    # pp_prepare
    'object': 'OBJECT',  # object name keyword
    'filter': 'FILTER',  # filter keyword
    'filter_translations': {'B': 'B', 'V': 'V',
                            'R': 'R', 'I': 'I',
                            'C': 'R'},
    # filtername translation dictionary
    'exptime': 'EXPTIME',  # exposure time keyword (s)
    'airmass': 'AIRMASS',  # airmass keyword

    # source extractor settings
    'source_minarea': 12,  # default sextractor source minimum N_pixels
    'source_snr': 3,  # default sextractor source snr for registration
    'aprad_default': 10,  # default aperture radius in px
    'aprad_range': [2, 15],  # [minimum, maximum] aperture radius (px)
    'sex-config-file': rootpath + '/setup/rbt.sex',
    'mask_file': {},
    #                        mask files as a function of x,y binning

    # scamp settings
    'scamp-config-file': rootpath + '/setup/rbt.scamp',
    'reg_max_mag': 19,
    'reg_search_radius': 0.5,  # deg
    'source_tolerance': 'high',
    
    # swarp settings
    'copy_keywords': ('OBJNAME,EXPOSURE,FILTER,DATE,JD'),
    #                        keywords to be copied in image
    #                        combination using swarp
    'swarp-config-file': rootpath+'/setup/rbt.swarp',

    # default catalog settings
    'astrometry_catalogs': ['GAIA'],
    'photometry_catalogs': ['PANSTARRS', 'SDSS-R9', 'APASS9', '2MASS']
}
# add telescope configurations to 'official' telescopes.py
implemented_telescopes.append('PST1v2')
# translate INSTRUME (or others, see _pp_conf.py) header keyword into PP telescope keyword
instrument_identifiers['SBIG ST-7'] = 'PST1v2'
# translate telescope keyword into parameter set defined here
telescope_parameters['PST1v2'] = pst1_v2_param






#-----------------------------------------------------------------------------
# DOAO: 1.0-m telescope in South Korea
doao_param = {
    'telescope_instrument': 'Dirver for Princeton Instruments cameras',  # telescope/instrument name
    'telescope_keyword': 'DOAO',  # telescope/instrument keyword
    'observatory_code': 'P66',   # MPC observatory code
    'secpix': (0.39, 0.39),    # pixel size (arcsec) before binning

    # image orientation preferences
    'flipx': True,
    'flipy': False,
    'rotate': 0,

    # instrument-specific FITS header keywords
    'binning': (3, 3),  # binning in x/y
    'extent': ('NAXIS1', 'NAXIS2'),  # N_pixels in x/y
    'ra': 'RA',  # telescope pointing, RA
    'dec': 'DEC',  # telescope pointin, Dec
    'radec_separator': ' ',  # RA/Dec hms separator, use 'XXX'
    # if already in degrees
    'date_keyword': 'DATE-OBS',  # obs date/time
    # keyword; use
    # 'date|time' if
    # separate
    'obsmidtime_jd': '',  # obs midtime jd keyword
    # (usually provided by
    # pp_prepare
    'object': 'OBJECT',  # object name keyword
    'filter': 'FILTER',  # filter keyword
    'filter_translations': {'B': 'B', 'V': 'V',
                            'R': 'R', 'I': 'I',
                            'Clear': 'R'},
    # filtername translation dictionary
    'exptime': 'EXPTIME',  # exposure time keyword (s)
    'airmass': 'AIRMASS',  # airmass keyword

    # source extractor settings
    'source_minarea': 12,  # default sextractor source minimum N_pixels
    'source_snr': 3,  # default sextractor source snr for registration
    'aprad_default': 6,  # default aperture radius in px
    'aprad_range': [2, 15],  # [minimum, maximum] aperture radius (px)
    'sex-config-file': rootpath + '/setup/rbt.sex',
    'mask_file': {},
    #                        mask files as a function of x,y binning

    # scamp settings
    'scamp-config-file': rootpath + '/setup/rbt.scamp',
    'reg_max_mag': 19,
    'reg_search_radius': 0.5,  # deg
    'source_tolerance': 'high',
    
    # swarp settings
    'copy_keywords': ('OBJNAME,EXPOSURE,FILTER,DATE,JD'),
    #                        keywords to be copied in image
    #                        combination using swarp
    'swarp-config-file': rootpath+'/setup/rbt.swarp',

    # default catalog settings
    'astrometry_catalogs': ['GAIA'],
    'photometry_catalogs': ['PANSTARRS', 'SDSS-R9', '2MASS']
}
# add telescope configurations to 'official' telescopes.py
implemented_telescopes.append('DOAO')
# translate INSTRUME (or others, see _pp_conf.py) header keyword into PP telescope keyword
instrument_identifiers['Dirver for Princeton Instruments cameras'] = 'DOAO'
# translate telescope keyword into parameter set defined here
telescope_parameters['DOAO'] = doao_param

#-----------------------------------------------------------------------------
# CAS: 0.6-m Schmidt telescope at Calar Alto
cas_param = {
    'telescope_instrument': 'ProLine PL230 #0',  # telescope/instrument name
    'telescope_keyword': 'CAS',  # telescope/instrument keyword
    'observatory_code': 'Z84',   # MPC observatory code
    'secpix': (1.29, 1.29),    # pixel size (arcsec) before binning

    # image orientation preferences
    'flipx': False,
    'flipy': False,
    'rotate': 180,

    # instrument-specific FITS header keywords
    'binning': (1, 1),  # binning in x/y
    'extent': ('NAXIS1', 'NAXIS2'),  # N_pixels in x/y
    'ra': 'RA',  # telescope pointing, RA
    'dec': 'DEC',  # telescope pointin, Dec
    'radec_separator': 'XXX',  # RA/Dec hms separator, use 'XXX'
    # if already in degrees
    'date_keyword': 'DATE-OBS',  # obs date/time
    # keyword; use
    # 'date|time' if
    # separate
    'obsmidtime_jd': '',  # obs midtime jd keyword
    # (usually provided by
    # pp_prepare
    'object': 'OBJECT',  # object name keyword
    'filter': 'FILTER',  # filter keyword
    'filter_translations': {'B': 'B', 'V': 'V',
                            'R': 'R', 'I': 'I',
                            'RG_Clear': 'R',
                            'SDSSi': 'i'},
    # filtername translation dictionary
    'exptime': 'EXPTIME',  # exposure time keyword (s)
    'airmass': 'AIRMASS',  # airmass keyword

    # source extractor settings
    'source_minarea': 12,  # default sextractor source minimum N_pixels
    'source_snr': 3,  # default sextractor source snr for registration
    'aprad_default': 6,  # default aperture radius in px
    'aprad_range': [2, 15],  # [minimum, maximum] aperture radius (px)
    'sex-config-file': rootpath + '/setup/rbt.sex',
    'mask_file': {},
    #                        mask files as a function of x,y binning

    # scamp settings
    'scamp-config-file': rootpath + '/setup/rbt.scamp',
    'reg_max_mag': 19,
    'reg_search_radius': 0.5,  # deg
    'source_tolerance': 'high',
    
    # swarp settings
    'copy_keywords': ('OBJNAME,EXPOSURE,FILTER,DATE,JD'),
    #                        keywords to be copied in image
    #                        combination using swarp
    'swarp-config-file': rootpath+'/setup/rbt.swarp',

    # default catalog settings
    'astrometry_catalogs': ['GAIA'],
    'photometry_catalogs': ['PANSTARRS', 'SDSS-R9', '2MASS']
}
# add telescope configurations to 'official' telescopes.py
implemented_telescopes.append('CAS')
# translate INSTRUME (or others, see _pp_conf.py) header keyword into PP telescope keyword
instrument_identifiers['ProLine PL230 #0'] = 'CAS'
# translate telescope keyword into parameter set defined here
telescope_parameters['CAS'] = cas_param

# ------------------------------------------------------------------------------
# ARO: 0.33-m, Abbey Ridge Obs., Canada
aro_param = {
    'telescope_instrument': '0.33-m, Abbey Ridge Obs., SBIG ST-8 Dual CCD Camera',  # telescope/instrument name
    'telescope_keyword': 'C14',  # telescope/instrument keyword
    'observatory_code': 'I22',   # MPC observatory code
    'secpix': (0.84, 0.84),    # pixel size (arcsec) before binning

    # image orientation preferences
    'flipx': False,
    'flipy': False,
    'rotate': 0,

    # instrument-specific FITS header keywords
    'binning': ('XBINNING', 'YBINNING'),  # binning in x/y
    'extent': ('NAXIS1', 'NAXIS2'),  # N_pixels in x/y
    'ra': 'RA',  # telescope pointing, RA
    'dec': 'DEC',  # telescope pointin, Dec
    'radec_separator': ' ',  # RA/Dec hms separator, use 'XXX'
    # if already in degrees
    'date_keyword': 'DATE-OBS',  # obs date/time
    # keyword; use
    # 'date|time' if
    # separate
    'obsmidtime_jd': '',  # obs midtime jd keyword
    # (usually provided by
    # pp_prepare
    'object': 'OBJECT',  # object name keyword
    'filter': 'FILTER',  # filter keyword
    'filter_translations': {'B': 'B', 'V': 'V',
                            'R': 'R', 'I': 'I',
                            'CLR': None},
    # filtername translation dictionary
    'exptime': 'EXPTIME',  # exposure time keyword (s)
    'airmass': 'AIRMASS',  # airmass keyword

    # source extractor settings
    'source_minarea': 12,  # default sextractor source minimum N_pixels
    'source_snr': 3,  # default sextractor source snr for registration
    'aprad_default': 6,  # default aperture radius in px
    'aprad_range': [2, 15],  # [minimum, maximum] aperture radius (px)
    'sex-config-file': rootpath + '/setup/rbt.sex',
    'mask_file': {},
    #                        mask files as a function of x,y binning

    # scamp settings
    'scamp-config-file': rootpath + '/setup/rbt.scamp',
    'reg_max_mag': 19,
    'reg_search_radius': 0.5,  # deg
    'source_tolerance': 'high',
    
    # swarp settings
    'copy_keywords': ('OBJNAME,EXPOSURE,FILTER,DATE,JD'),
    #                        keywords to be copied in image
    #                        combination using swarp
    'swarp-config-file': rootpath+'/setup/rbt.swarp',

    # default catalog settings
    'astrometry_catalogs': ['GAIA'],
    'photometry_catalogs': ['PANSTARRS', 'SDSS-R9', '2MASS']
}
# add telescope configurations to 'official' telescopes.py
implemented_telescopes.append('ARO')
# translate INSTRUME (or others, see _pp_conf.py) header keyword into PP telescope keyword
instrument_identifiers['SBIG ST-8 Dual CCD Camera'] = 'ARO'
# translate telescope keyword into parameter set defined here
telescope_parameters['ARO'] = aro_param

# ------------------------------------------------------------------------------
# BGO: 0.61-m, Burke-Gaffney Obs., Canada
bgo_param = {
    'telescope_instrument': '0.61-m, Burke-Gaffney Obs., Apogee CG-16M',  # telescope/instrument name
    'telescope_keyword': 'Apogee USB/Net',  # telescope/instrument keyword
    'observatory_code': '851',   # MPC observatory code
    'secpix': (0.47, 0.47),    # pixel size (arcsec) before binning

    # image orientation preferences
    'flipx': False,
    'flipy': False,
    'rotate': 180,

    # instrument-specific FITS header keywords
    'binning': ('XBINNING', 'YBINNING'),  # binning in x/y
    'extent': ('NAXIS1', 'NAXIS2'),  # N_pixels in x/y
    'ra': 'RA',  # telescope pointing, RA
    'dec': 'DEC',  # telescope pointin, Dec
    'radec_separator': ' ',  # RA/Dec hms separator, use 'XXX'
    # if already in degrees
    'date_keyword': 'DATE-OBS',  # obs date/time
    # keyword; use
    # 'date|time' if
    # separate
    'obsmidtime_jd': '',  # obs midtime jd keyword
    # (usually provided by
    # pp_prepare
    'object': 'OBJECT',  # object name keyword
    'filter': 'FILTER',  # filter keyword
    'filter_translations': {'B': 'B', 'V': 'V',
                            'R': 'R', 'I': 'I',
                            'SG': 'g', 'SI': 'i'},
    # filtername translation dictionary
    'exptime': 'EXPTIME',  # exposure time keyword (s)
    'airmass': 'AIRMASS',  # airmass keyword

    # source extractor settings
    'source_minarea': 12,  # default sextractor source minimum N_pixels
    'source_snr': 3,  # default sextractor source snr for registration
    'aprad_default': 6,  # default aperture radius in px
    'aprad_range': [2, 15],  # [minimum, maximum] aperture radius (px)
    'sex-config-file': rootpath + '/setup/rbt.sex',
    'mask_file': {},
    #                        mask files as a function of x,y binning

    # scamp settings
    'scamp-config-file': rootpath + '/setup/rbt.scamp',
    'reg_max_mag': 19,
    'reg_search_radius': 0.5,  # deg
    'source_tolerance': 'high',
    
    # swarp settings
    'copy_keywords': ('OBJNAME,EXPOSURE,FILTER,DATE,JD'),
    #                        keywords to be copied in image
    #                        combination using swarp
    'swarp-config-file': rootpath+'/setup/rbt.swarp',

    # default catalog settings
    'astrometry_catalogs': ['GAIA'],
    'photometry_catalogs': ['PANSTARRS', 'SDSS-R9', '2MASS']
}
# add telescope configurations to 'official' telescopes.py
implemented_telescopes.append('BGO')
# translate INSTRUME (or others, see _pp_conf.py) header keyword into PP telescope keyword
instrument_identifiers['Apogee USB/Net'] = 'BGO'
# translate telescope keyword into parameter set defined here
telescope_parameters['BGO'] = bgo_param

# ------------------------------------------------------------------------------
# PdM: 1-m, Pic du Midi Obs., France
PdM_param = {
    'telescope_instrument': '1-m, Pic du Midi Obs., CAMERA DZ936_BV Marconi libandorusb',  # telescope/instrument name
    'telescope_keyword': 't1m',  # telescope/instrument keyword
    'observatory_code': '586',   # MPC observatory code
    'secpix': (0.248, 0.248),    # pixel size (arcsec) before binning

    # image orientation preferences
    'flipx': False,
    'flipy': False,
    'rotate': 0,

    # instrument-specific FITS header keywords
    'binning': ('BIN1', 'BIN2'),  # binning in x/y
    'extent': ('NAXIS1', 'NAXIS2'),  # N_pixels in x/y
    'ra': 'OBJCTRA',  # telescope pointing, RA
    'dec': 'OBJCTDEC',  # telescope pointin, Dec
    'radec_separator': ' ',  # RA/Dec hms separator, use 'XXX'
    # if already in degrees
    'date_keyword': 'DATE-OBS',  # obs date/time
    # keyword; use
    # 'date|time' if
    # separate
    'obsmidtime_jd': '',  # obs midtime jd keyword
    # (usually provided by
    # pp_prepare
    'object': 'OBJECT',  # object name keyword
    'filter': 'FILTERS',  # filter keyword
    'filter_translations': {'Gp': 'g', 'Rp': 'r',
                            'Ip': 'i', 'Zp': 'z'},
    # filtername translation dictionary
    'exptime': 'EXPOSURE',  # exposure time keyword (s)
    'airmass': 'AIRMASS',  # airmass keyword

    # source extractor settings
    'source_minarea': 12,  # default sextractor source minimum N_pixels
    'source_snr': 3,  # default sextractor source snr for registration
    'aprad_default': 6,  # default aperture radius in px
    'aprad_range': [2, 15],  # [minimum, maximum] aperture radius (px)
    'sex-config-file': rootpath + '/setup/rbt.sex',
    'mask_file': {},
    #                        mask files as a function of x,y binning

    # scamp settings
    'scamp-config-file': rootpath + '/setup/rbt.scamp',
    'reg_max_mag': 19,
    'reg_search_radius': 0.5,  # deg
    'source_tolerance': 'high',
    
    # swarp settings
    'copy_keywords': ('OBJECT,EXPOSURE,FILTERS,DATE'),
    #                        keywords to be copied in image
    #                        combination using swarp
    'swarp-config-file': rootpath+'/setup/rbt.swarp',

    # default catalog settings
    'astrometry_catalogs': ['GAIA'],
    'photometry_catalogs': ['PANSTARRS', 'SDSS-R9', '2MASS']
}
# add telescope configurations to 'official' telescopes.py
implemented_telescopes.append('PdM')
# translate INSTRUME (or others, see _pp_conf.py) header keyword into PP telescope keyword
instrument_identifiers['t1m'] = 'PdM'
# translate telescope keyword into parameter set defined here
telescope_parameters['PdM'] = PdM_param

#-----------------------------------------------------------------------------
# Schiaparelli: 0.8-m telescope, G.V. Schiaparelli Astronomical Observatory, Varese, Italy
Schiaparelli_param = {
    'telescope_instrument': '0.8-m telescope, G.V. Schiaparelli Astronomical Observatory, Varese, Italy',  # telescope/instrument name
    'telescope_keyword': 'SBIG STX-16803',  # telescope/instrument keyword
    'observatory_code': '204',   # MPC observatory code
    'secpix': (0.623, 0.623),    # pixel size (arcsec) before binning

    # image orientation preferences
    'flipx': True,
    'flipy': True,
    'rotate': 0,

    # instrument-specific FITS header keywords
    'binning': ('XBINNING', 'YBINNING'),  # binning in x/y
    'extent': ('NAXIS1', 'NAXIS2'),  # N_pixels in x/y
    'ra': 'CRVAL1',  # telescope pointing, RA
    'dec': 'CRVAL2',  # telescope pointin, Dec
    'radec_separator': 'XXX',  # RA/Dec hms separator, use 'XXX'
    # if already in degrees
    'date_keyword': 'DATE-OBS',  # obs date/time
    # keyword; use
    # 'date|time' if
    # separate
    'obsmidtime_jd': '',  # obs midtime jd keyword
    # (usually provided by
    # pp_prepare
    'object': 'OBJECT',  # object name keyword
    'filter': 'FILTER',  # filter keyword
    'filter_translations': {'None': 'R', 'V': 'V',
                            'R': 'R', 'I': 'I',
                            },
    # filtername translation dictionary
    'exptime': 'EXPTIME',  # exposure time keyword (s)
    'airmass': 'AIRMASS',  # airmass keyword

    # source extractor settings
    'source_minarea': 12,  # default sextractor source minimum N_pixels
    'source_snr': 3,  # default sextractor source snr for registration
    'aprad_default': 10,  # default aperture radius in px
    'aprad_range': [2, 15],  # [minimum, maximum] aperture radius (px)
    'sex-config-file': rootpath + '/setup/rbt.sex',
    'mask_file': {},
    #                        mask files as a function of x,y binning

    # scamp settings
    'scamp-config-file': rootpath + '/setup/rbt.scamp',
    'reg_max_mag': 19,
    'reg_search_radius': 0.5,  # deg
    'source_tolerance': 'high',
    
    # swarp settings
    'copy_keywords': ('OBJNAME,EXPOSURE,FILTER,DATE,JD'),
    #                        keywords to be copied in image
    #                        combination using swarp
    'swarp-config-file': rootpath+'/setup/rbt.swarp',

    # default catalog settings
    'astrometry_catalogs': ['GAIA'],
    'photometry_catalogs': ['PANSTARRS', 'SDSS-R9', 'APASS9', '2MASS']
}
# add telescope configurations to 'official' telescopes.py
implemented_telescopes.append('Schiaparelli')
# translate INSTRUME (or others, see _pp_conf.py) header keyword into PP telescope keyword
instrument_identifiers['SBIG STX-16803'] = 'Schiaparelli'
# translate telescope keyword into parameter set defined here
telescope_parameters['Schiaparelli'] = Schiaparelli_param
#-----------------------------------------------------------------------------
# GreatShefford: 0.4-m telescope Great Shefford Observatory, United Kingdom
GreatShefford_param = {
    'telescope_instrument': '0.4-m telescope Great Shefford Observatory, United Kingdom',  # telescope/instrument name
    'telescope_keyword': 'Great Shefford Observatory, Apogee USB/Net',  # telescope/instrument keyword
    'observatory_code': 'J95',   # MPC observatory code
    'secpix': (1.08,1.08),    # pixel size (arcsec) before binning

    # image orientation preferences
    'flipx': True,
    'flipy': True,
    'rotate': 0,

    # instrument-specific FITS header keywords
    'binning': ('XBINNING', 'YBINNING'),  # binning in x/y
    'extent': ('NAXIS1', 'NAXIS2'),  # N_pixels in x/y
    'ra': 'OBJCTRA',  # telescope pointing, RA
    'dec': 'OBJCTDEC',  # telescope pointin, Dec
    'radec_separator': ' ',  # RA/Dec hms separator, use 'XXX'
    # if already in degrees
    'date_keyword': 'DATE-OBS',  # obs date/time
    # keyword; use
    # 'date|time' if
    # separate
    'obsmidtime_jd': '',  # obs midtime jd keyword
    # (usually provided by
    # pp_prepare
    'object': 'OBJECT',  # object name keyword
    'filter': 'FILTER',  # filter keyword
    'filter_translations': {'C': 'R', 'V': 'V',
                            'R': 'R', 'I': 'I',
                            },
    # filtername translation dictionary
    'exptime': 'EXPTIME',  # exposure time keyword (s)
    'airmass': 'AIRMASS',  # airmass keyword

    # source extractor settings
    'source_minarea': 12,  # default sextractor source minimum N_pixels
    'source_snr': 3,  # default sextractor source snr for registration
    'aprad_default': 10,  # default aperture radius in px
    'aprad_range': [2, 15],  # [minimum, maximum] aperture radius (px)
    'sex-config-file': rootpath + '/setup/rbt.sex',
    'mask_file': {},
    #                        mask files as a function of x,y binning

    # scamp settings
    'scamp-config-file': rootpath + '/setup/rbt.scamp',
    'reg_max_mag': 19,
    'reg_search_radius': 0.5,  # deg
    'source_tolerance': 'high',
    
    # swarp settings
    'copy_keywords': ('OBJNAME,EXPOSURE,FILTER,DATE,JD'),
    #                        keywords to be copied in image
    #                        combination using swarp
    'swarp-config-file': rootpath+'/setup/rbt.swarp',

    # default catalog settings
    'astrometry_catalogs': ['GAIA'],
    'photometry_catalogs': ['PANSTARRS', 'SDSS-R9', 'APASS9', '2MASS']
}
# add telescope configurations to 'official' telescopes.py
implemented_telescopes.append('GreatShefford')
# translate INSTRUME (or others, see _pp_conf.py) header keyword into PP telescope keyword
instrument_identifiers['Great Shefford Observatory, Apogee USB/Net'] = 'GreatShefford'
# translate telescope keyword into parameter set defined here
telescope_parameters['GreatShefford'] = GreatShefford_param

#-----------------------------------------------------------------------------
# Konkoly:  Konkoly Observatory, Hungary
Konkoly_param = {
    'telescope_instrument': '0.8-m telescope, Konkoly Observatory, Hungary',  # telescope/instrument name
    'telescope_keyword': 'FLI Microline',  # telescope/instrument keyword
    'observatory_code': '053',   # MPC observatory code
    'secpix': (0.55, 0.55),    # pixel size (arcsec) before binning

    # image orientation preferences
    'flipx': False,
    'flipy': False,
    'rotate': 0,

    # instrument-specific FITS header keywords
    'binning': ('CCDXBIN', 'CCDYBIN'),  # binning in x/y
    'extent': ('NAXIS1', 'NAXIS2'),  # N_pixels in x/y
    'ra': 'RA',  # telescope pointing, RA
    'dec': 'DEC',  # telescope pointin, Dec
    'radec_separator': ':',  # RA/Dec hms separator, use 'XXX'
    # if already in degrees
    'date_keyword': 'DATE-OBS',  # obs date/time
    # keyword; use
    # 'date|time' if
    # separate
    'obsmidtime_jd': '',  # obs midtime jd keyword
    # (usually provided by
    # pp_prepare
    'object': 'OBJECT',  # object name keyword
    'filter': 'FILTER',  # filter keyword
    'filter_translations': {'r': 'r'},
    # filtername translation dictionary
    'exptime': 'EXPTIME',  # exposure time keyword (s)
    'airmass': 'AIRMASS',  # airmass keyword

    # source extractor settings
    'source_minarea': 12,  # default sextractor source minimum N_pixels
    'source_snr': 3,  # default sextractor source snr for registration
    'aprad_default': 6,  # default aperture radius in px
    'aprad_range': [2, 15],  # [minimum, maximum] aperture radius (px)
    'sex-config-file': rootpath + '/setup/rbt.sex',
    'mask_file': {},
    #                        mask files as a function of x,y binning

    # scamp settings
    'scamp-config-file': rootpath + '/setup/rbt.scamp',
    'reg_max_mag': 19,
    'reg_search_radius': 0.5,  # deg
    'source_tolerance': 'high',
    
    # swarp settings
    'copy_keywords': ('OBJNAME,EXPOSURE,FILTER,DATE,JD'),
    #                        keywords to be copied in image
    #                        combination using swarp
    'swarp-config-file': rootpath+'/setup/rbt.swarp',

    # default catalog settings
    'astrometry_catalogs': ['GAIA'],
    'photometry_catalogs': ['PANSTARRS', 'SDSS-R9', '2MASS']
}
# add telescope configurations to 'official' telescopes.py
implemented_telescopes.append('Konkoly')
# translate INSTRUME (or others, see _pp_conf.py) header keyword into PP telescope keyword
instrument_identifiers['FLI Microline'] = 'Konkoly'
# translate telescope keyword into parameter set defined here
telescope_parameters['Konkoly'] = Konkoly_param


#-----------------------------------------------------------------------------
# IAC80: 0.8-m telescope at Teide Observatory
IAC80_param = {
    'telescope_instrument': 'IAC80: 0.8-m telescope at Teide Observatory',  # telescope/instrument name
    'telescope_keyword': 'IAC80 telescope',  # telescope/instrument keyword
    'observatory_code': '954',   # MPC observatory code
    'secpix': (0.322,0.322),    # pixel size (arcsec) before binning

    # image orientation preferences
    'flipx': True,
    'flipy': True,
    'rotate': 0,

    # instrument-specific FITS header keywords
    'binning': (1,1),  # binning in x/y
    'extent': ('NAXIS1', 'NAXIS2'),  # N_pixels in x/y
    'ra': 'RA',  # telescope pointing, RA
    'dec': 'DEC',  # telescope pointin, Dec
    'radec_separator': ' ',  # RA/Dec hms separator, use 'XXX'
    # if already in degrees
    'date_keyword': 'DATE',  # obs date/time
    # keyword; use
    # 'date|time' if
    # separate
    'obsmidtime_jd': '',  # obs midtime jd keyword
    # (usually provided by
    # pp_prepare
    'object': 'OBJECT',  # object name keyword
    'filter': 'INSFILTE',  # filter keyword
    'filter_translations': {'OPEN': 'V', 'V': 'V',
                            'R': 'R', 'I': 'I',
                            },
    # filtername translation dictionary
    'exptime': 'EXPTIME',  # exposure time keyword (s)
    'airmass': 'AIRMASS',  # airmass keyword

    # source extractor settings
    'source_minarea': 12,  # default sextractor source minimum N_pixels
    'source_snr': 3,  # default sextractor source snr for registration
    'aprad_default': 10,  # default aperture radius in px
    'aprad_range': [2, 15],  # [minimum, maximum] aperture radius (px)
    'sex-config-file': rootpath + '/setup/rbt.sex',
    'mask_file': {},
    #                        mask files as a function of x,y binning

    # scamp settings
    'scamp-config-file': rootpath + '/setup/rbt.scamp',
    'reg_max_mag': 19,
    'reg_search_radius': 0.5,  # deg
    'source_tolerance': 'high',
    
    # swarp settings
    'copy_keywords': ('OBJNAME,EXPOSURE,FILTER,DATE,JD'),
    #                        keywords to be copied in image
    #                        combination using swarp
    'swarp-config-file': rootpath+'/setup/rbt.swarp',

    # default catalog settings
    'astrometry_catalogs': ['GAIA'],
    'photometry_catalogs': ['PANSTARRS', 'SDSS-R9', 'APASS9', '2MASS']
}
# add telescope configurations to 'official' telescopes.py
implemented_telescopes.append('IAC80')
# translate INSTRUME (or others, see _pp_conf.py) header keyword into PP telescope keyword
instrument_identifiers['1100.144.0'] = 'IAC80'
# translate telescope keyword into parameter set defined here
telescope_parameters['IAC80'] = IAC80_param

#-----------------------------------------------------------------------------
# SMdM: Remote Observatory Santa Maria de Montmagastrell, Tarrega, Spain
SMdM_param = {
    'telescope_instrument': 'SBIG STL-1001 3 CCD Camera, Remote Observatory Santa Maria de Montmagastrell, Tarrega, Spain',  # telescope/instrument name
    'telescope_keyword': 'SBIG STL-1001 3 CCD Camera',  # telescope/instrument keyword
    'observatory_code': 'B74',   # MPC observatory code
    'secpix': (1.24,1.24),    # pixel size (arcsec) before binning

    # image orientation preferences
    'flipx': True,
    'flipy': True,
    'rotate': 0,

    # instrument-specific FITS header keywords
    'binning': ('XBINNING', 'YBINNING'),  # binning in x/y
    'extent': ('NAXIS1', 'NAXIS2'),  # N_pixels in x/y
    'ra': 'OBJCTRA',  # telescope pointing, RA
    'dec': 'OBJCTDEC',  # telescope pointin, Dec
    'radec_separator': ' ',  # RA/Dec hms separator, use 'XXX'
    # if already in degrees
    'date_keyword': 'DATE-OBS',  # obs date/time
    # keyword; use
    # 'date|time' if
    # separate
    'obsmidtime_jd': '',  # obs midtime jd keyword
    # (usually provided by
    # pp_prepare
    'object': 'OBJECT',  # object name keyword
    'filter': 'FILTER',  # filter keyword
    'filter_translations': {
                            'R': 'R'
                            },
    # filtername translation dictionary
    'exptime': 'EXPTIME',  # exposure time keyword (s)
    'airmass': 'AIRMASS',  # airmass keyword

    # source extractor settings
    'source_minarea': 12,  # default sextractor source minimum N_pixels
    'source_snr': 3,  # default sextractor source snr for registration
    'aprad_default': 10,  # default aperture radius in px
    'aprad_range': [2, 15],  # [minimum, maximum] aperture radius (px)
    'sex-config-file': rootpath + '/setup/rbt.sex',
    'mask_file': {},
    #                        mask files as a function of x,y binning

    # scamp settings
    'scamp-config-file': rootpath + '/setup/rbt.scamp',
    'reg_max_mag': 19,
    'reg_search_radius': 0.5,  # deg
    'source_tolerance': 'high',
    
    # swarp settings
    'copy_keywords': ('OBJNAME,EXPOSURE,FILTER,DATE,JD'),
    #                        keywords to be copied in image
    #                        combination using swarp
    'swarp-config-file': rootpath+'/setup/rbt.swarp',

    # default catalog settings
    'astrometry_catalogs': ['GAIA'],
    'photometry_catalogs': ['PANSTARRS', 'SDSS-R9', 'APASS9', '2MASS']
}
# add telescope configurations to 'official' telescopes.py
implemented_telescopes.append('SMdM')
# translate INSTRUME (or others, see _pp_conf.py) header keyword into PP telescope keyword
instrument_identifiers['SBIG STL-1001 3 CCD Camera'] = 'SMdM'
# translate telescope keyword into parameter set defined here
telescope_parameters['SMdM'] = SMdM_param

#-----------------------------------------------------------------------------
# C2PU: 1-m telescope at Observatoire de la Cote d�Azur, Universit� de Nice Sophia-Antipolis
C2PU_param = {
    'telescope_instrument': 'C2PU: 1-m telescope at Observatoire de la Cote dAzur',  # telescope/instrument name
    'telescope_keyword': 'C2PU',  # telescope/instrument keyword
    'observatory_code': '010',   # MPC observatory code
    'secpix': (0.85, 0.85),    # pixel size (arcsec) before binning

    # image orientation preferences
    'flipx': False,
    'flipy': True,
    'rotate': 0,

    # instrument-specific FITS header keywords
    'binning': (1,1),  # binning in x/y
    'extent': ('NAXIS1', 'NAXIS2'),  # N_pixels in x/y
    'ra': 'OBJCTRA',  # telescope pointing, RA
    'dec': 'OBJCTDEC',  # telescope pointin, Dec
    'radec_separator': ' ',  # RA/Dec hms separator, use 'XXX'
    # if already in degrees
    'date_keyword': 'DATE-OBS',  # obs date/time
    # keyword; use
    # 'date|time' if
    # separate
    'obsmidtime_jd': '',  # obs midtime jd keyword
    # (usually provided by
    # pp_prepare
    'object': 'OBJECT',  # object name keyword
    'filter': 'FILTERS',  # filter keyword
    'filter_translations': {'OPEN': 'V', 'V': 'V',
                            'R': 'R', 'I': 'I',
                            },
    # filtername translation dictionary
    'exptime': 'EXPOSURE',  # exposure time keyword (s)
    'airmass': 'AIRMASS',  # airmass keyword

    # source extractor settings
    'source_minarea': 12,  # default sextractor source minimum N_pixels
    'source_snr': 3,  # default sextractor source snr for registration
    'aprad_default': 10,  # default aperture radius in px
    'aprad_range': [2, 15],  # [minimum, maximum] aperture radius (px)
    'sex-config-file': rootpath + '/setup/rbt.sex',
    'mask_file': {},
    #                        mask files as a function of x,y binning

    # scamp settings
    'scamp-config-file': rootpath + '/setup/rbt.scamp',
    'reg_max_mag': 19,
    'reg_search_radius': 0.5,  # deg
    'source_tolerance': 'high',
    
    # swarp settings
    'copy_keywords': ('OBJNAME,EXPOSURE,FILTER,DATE,JD'),
    #                        keywords to be copied in image
    #                        combination using swarp
    'swarp-config-file': rootpath+'/setup/rbt.swarp',

    # default catalog settings
    'astrometry_catalogs': ['GAIA'],
    'photometry_catalogs': ['PANSTARRS', 'SDSS-R9', 'APASS9', '2MASS']
}
# add telescope configurations to 'official' telescopes.py
implemented_telescopes.append('C2PU')
# translate INSTRUME (or others, see _pp_conf.py) header keyword into PP telescope keyword
instrument_identifiers['C2PU'] = 'C2PU'
# translate telescope keyword into parameter set defined here
telescope_parameters['C2PU'] = C2PU_param

#-----------------------------------------------------------------------------
# newSMdM: Remote Observatory Santa Maria de Montmagastrell, Tarrega, Spain, new CCD
newSMdM_param = {
    'telescope_instrument': 'SBIG STL-11000 3 CCD Camera, Remote Observatory Santa Maria de Montmagastrell, Tarrega, Spain',  # telescope/instrument name
    'telescope_keyword': 'SBIG STL-11000 3 CCD Camera',  # telescope/instrument keyword
    'observatory_code': 'B74',   # MPC observatory code
    'secpix': (0.914,0.914),    # pixel size (arcsec) before binning

    # image orientation preferences
    'flipx': True,
    'flipy': True,
    'rotate': 0,

    # instrument-specific FITS header keywords
    'binning': ('XBINNING', 'YBINNING'),  # binning in x/y
    'extent': ('NAXIS1', 'NAXIS2'),  # N_pixels in x/y
    'ra': 'OBJCTRA',  # telescope pointing, RA
    'dec': 'OBJCTDEC',  # telescope pointin, Dec
    'radec_separator': ' ',  # RA/Dec hms separator, use 'XXX'
    # if already in degrees
    'date_keyword': 'DATE-OBS',  # obs date/time
    # keyword; use
    # 'date|time' if
    # separate
    'obsmidtime_jd': '',  # obs midtime jd keyword
    # (usually provided by
    # pp_prepare
    'object': 'OBJECT',  # object name keyword
    'filter': 'FILTER',  # filter keyword
    'filter_translations': {
                            'R': 'R'
                            },
    # filtername translation dictionary
    'exptime': 'EXPTIME',  # exposure time keyword (s)
    'airmass': 'AIRMASS',  # airmass keyword

    # source extractor settings
    'source_minarea': 12,  # default sextractor source minimum N_pixels
    'source_snr': 3,  # default sextractor source snr for registration
    'aprad_default': 10,  # default aperture radius in px
    'aprad_range': [2, 15],  # [minimum, maximum] aperture radius (px)
    'sex-config-file': rootpath + '/setup/rbt.sex',
    'mask_file': {},
    #                        mask files as a function of x,y binning

    # scamp settings
    'scamp-config-file': rootpath + '/setup/rbt.scamp',
    'reg_max_mag': 19,
    'reg_search_radius': 0.5,  # deg
    'source_tolerance': 'high',
    
    # swarp settings
    'copy_keywords': ('OBJNAME,EXPOSURE,FILTER,DATE,JD'),
    #                        keywords to be copied in image
    #                        combination using swarp
    'swarp-config-file': rootpath+'/setup/rbt.swarp',

    # default catalog settings
    'astrometry_catalogs': ['GAIA'],
    'photometry_catalogs': ['PANSTARRS', 'SDSS-R9', 'APASS9', '2MASS']
}
# add telescope configurations to 'official' telescopes.py
implemented_telescopes.append('newSMdM')
# translate INSTRUME (or others, see _pp_conf.py) header keyword into PP telescope keyword
instrument_identifiers['SBIG STL-11000 3 CCD Camera'] = 'newSMdM'
# translate telescope keyword into parameter set defined here
telescope_parameters['newSMdM'] = newSMdM_param

#-----------------------------------------------------------------------------

