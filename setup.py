import cx_Freeze


cx_Freeze.setup(
    name='hebrew-bot',
    version='0.0.1',
    description='Telegram bot which uses API of hebcal.com',
    options={
        'build_exe': {
            'include_files': 'src/.env'
        }
    },
    executables=[cx_Freeze.Executable('src/bot.py')]
)
