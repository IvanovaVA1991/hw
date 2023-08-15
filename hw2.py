import subprocess

def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    print(result.stdout)
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False

def getout(cmd):
    return subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8').stdout


folder_in = '/home/user/tst'
folder_out = '/home/user/out'

print(checkout('cd /home/user/tst; 7z a /home/user/arh1', 'Everything is Ok'))

def test_step1():
    assert checkout(f'cd {folder_in}; 7z a {folder_out}/arh1', 'Everything is Ok'), 'test_step1 False'


def test_step2():
    assert checkout(f'cd {folder_in}; 7z u {folder_out}/arh1', 'Everything is Ok'), 'test_step2 False'

def test_step3():
    assert checkout(f'cd {folder_in}; 7z d {folder_out}/arh1', 'Everything is Ok'), 'test_step3 False'

def test_step4():
    assert checkout(f'cd {folder_out}; 7z l arh1.7z', '2 files'), 'test4 fail'


def test_step5():
    hash = getout(f'cd {folder_out}; crc32 arh1.7z').upper()
    assert checkout(f'cd {folder_out}; 7z h arh1.7z', hash), 'test5 fail'
