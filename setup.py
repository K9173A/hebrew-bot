import cx_Freeze


cx_Freeze.setup(
    name='hebrew-bot',
    version='0.0.1',
    description='Telegram bot which uses API of hebcal.com',
    options={
        'build_exe': {
            'include_files': 'src/.env',
            'excludes': [
                'lib2to3',
                'multiprocessing',
                'test',
                'tkinter',
                'unittest',
                'xml',
                'xmlrpc'
            ],
            'optimize': 2
        }
    },
    executables=[cx_Freeze.Executable('src/bot.py')]
)
