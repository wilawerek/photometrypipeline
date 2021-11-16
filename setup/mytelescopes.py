"""
Personal Photometry Pipeline Configuation File
2016-11-01, mommermiscience@gmail.com

Telescopes setup for automated photometry
for
Astronomical Observatory Institute
Faculty of Physics
Adam Mickiewicz University in Poznań

modified: 2021-10-13 by EWil

2021-11-07 TK: Added definition of PIT
               Corrected definitions of RBT, UBC

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

# RBT
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
    'flipy': True,
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

# ------------------------------------------------------------------------------
 
 