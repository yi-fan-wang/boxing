import lal
import numpy as np
import pycbc.waveform
import pycbc.pnutils

def gen_imrphenomtphmj(**par):
    if "approximant" in par:
        par.pop("approximant")
    hlms = pycbc.waveform.get_td_waveform_modes(approximant='IMRPhenomTPHM_J', **par)
    out = None
    for mode in hlms:
        l, m = mode
        hlm = hlms[l, m][0] + 1j * hlms[l, m][1]
        ylm = lal.SpinWeightedSphericalHarmonic(par['inclination'], np.pi/2 - par['coa_phase'], -2, l, m)
        if out is None:
            out = hlm * ylm
        else:
            out += hlm * ylm
    return out.real(), -out.imag()

def get_imrphenomtphmj_length(**kwargs):
    kwargs['f_lower'] = kwargs['f_lower'] / 5 * 2
    return pycbc.pnutils.get_imr_duration(kwargs['mass1'],
                                          kwargs['mass2'],
                                          kwargs['spin1z'],
                                          kwargs['spin2z'],
                                          kwargs['f_lower'],
                                          approximant='IMRPhenomXAS')