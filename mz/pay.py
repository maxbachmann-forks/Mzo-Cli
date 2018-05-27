import maya

from mz import arguments, options
from mz.utils import command


@command()
@arguments.name()
@arguments.amount()
@options.sort_code()
@options.account_number()
@options.message()
@options.on_datetime()
@options.daily_frequency_flag()
@options.weekly_frequency_flag()
@options.monthly_frequency_flag()
@options.yearly_frequency_flag()
@options.user_defined_frequency()
async def pay(name, amount, sort_code, account_number, message, on, every):
    print('paying:', name)
    print('amount:', amount)
    print('sort_code:', sort_code)
    print('account_number:', account_number)
    print('message:', message)
    print('on:', maya.when(on).slang_date())
    print('every:', every)
