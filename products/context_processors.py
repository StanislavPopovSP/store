from products.models import Basket


def baskets(requers):
    user = requers.user
    return {'baskets': Basket.objects.filter(user=user) if user.is_authenticated else []}
