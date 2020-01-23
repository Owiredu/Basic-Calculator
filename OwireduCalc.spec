# -*- mode: python -*-

block_cipher = None


a = Analysis(['calc.py'],
             pathex=['/home/owiredu/Desktop'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
a.datas+=[('calculator.png', '/home/owiredu/Desktop/calculator.png', 'DATA')]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='OwireduCalc',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
