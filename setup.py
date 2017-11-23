from distutils.core import setup

setup(
    name='moneywave-python',
    version='v1.0-beta',
    packages=['test', 'moneywave', 'moneywave.utils', 'moneywave.wallet',
              'moneywave.wallet.funding', 'moneywave.wallet.transfer',
              'moneywave.account', 'moneywave.resources',
              'moneywave.transaction'],
    url='https://github.com/alekaizer/moneywave-python',
    license='MIT',
    author='Achille AROUKO',
    author_email='achille.arouko@gmail.com',
    description='MoneyWave Python Library'
)
