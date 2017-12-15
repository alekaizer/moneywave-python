from distutils.core import setup

setup(
    name='moneywave',
    version='v1.1',
    packages=['moneywave', 'moneywave.utils', 'moneywave.wallet',
              'moneywave.wallet.funding', 'moneywave.wallet.transfer',
              'moneywave.account', 'moneywave.resources',
              'moneywave.transaction'],
    url='https://github.com/alekaizer/moneywave-python',
    license='MIT',
    author='Achille AROUKO',
    author_email='achille.arouko@gmail.com',
    description='MoneyWave Python Library'
)
