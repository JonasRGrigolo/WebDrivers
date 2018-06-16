from behave import given, when, then

def sum_of_items(items_list):
    return sum(items_list)

def sum_of_values(items_values):
    return sum(items_values)


@given('The user adds {num:d} product to shop cart')
def items_in_shop_cart(context, num):
        context.items = num


@when('He adds {num:d} more products on the shop cart')
def new_items_in_shop_cart(context, num):
        context.new_items = num


@then('The total number of items in shop cart shall be equal to {num:d}')
def total_items_in_shop_cart(context, num):
    assert sum_of_items(
            [context.items, context.new_items]
    ) == num


@given('The user added a product in shop cart with value {num:d}')
def item1_value(context, num):
        context.item1 = num


@when('The user adds another product in shop cart with value {num:d}')
def item2_value(context, num):
        context.item2 = num


@then('the total value of products in shop cart shall be {num:d}')
def total_items_in_shop_cart(context, num):
    assert sum_of_values(
            [context.item1, context.item2]
    ) == num