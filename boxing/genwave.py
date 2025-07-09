import lal
import numpy as np
import pycbc.waveform

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
