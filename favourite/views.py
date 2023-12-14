from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product, Variation
from .models import fav, favItem
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse



def _fav_id(request):
    fav = request.session.session_key
    if not fav:
        fav = request.session.create()
    return fav

def add_fav(request, product_id):
    current_user = request.user
    product = Product.objects.get(id=product_id) #get the product
    # If the user is authenticated
    if current_user.is_authenticated:
        product_variation = []
        if request.method == 'POST':
            for item in request.POST:
                key = item
                value = request.POST[key]

                try:
                    variation = Variation.objects.get(product=product, variation_category__iexact=key, variation_value__iexact=value)
                    product_variation.append(variation)
                except:
                    pass


        is_fav_item_exists = favItem.objects.filter(product=product, user=current_user).exists()
        if is_fav_item_exists:
            fav_item = favItem.objects.filter(product=product, user=current_user)
            ex_var_list = []
            id = []
            for item in fav_item:
                existing_variation = item.variations.all()
                ex_var_list.append(list(existing_variation))
                id.append(item.id)

            if product_variation in ex_var_list:
                # increase the fav item quantity
                index = ex_var_list.index(product_variation)
                item_id = id[index]
                item = favItem.objects.get(product=product, id=item_id)
                item.quantity += 1
                item.save()

            else:
                item = favItem.objects.create(product=product, quantity=1, user=current_user)
                if len(product_variation) > 0:
                    item.variations.clear()
                    item.variations.add(*product_variation)
                item.save()
        else:
            fav_item = favItem.objects.create(
                product = product,
                quantity = 1,
                user = current_user,
            )
            if len(product_variation) > 0:
                fav_item.variations.clear()
                fav_item.variations.add(*product_variation)
            fav_item.save()
        return redirect('favourite')
    # If the user is not authenticated
    else:
        product_variation = []
        if request.method == 'POST':
            for item in request.POST:
                key = item
                value = request.POST[key]

                try:
                    variation = Variation.objects.get(product=product, variation_category__iexact=key, variation_value__iexact=value)
                    product_variation.append(variation)
                except:
                    pass


        try:
            fav = fav.objects.get(fav_id=_fav_id(request)) # get the fav using the fav_id present in the session
        except fav.DoesNotExist:
            fav = fav.objects.create(
                fav_id = _fav_id(request)
            )
        fav.save()

        is_fav_item_exists = favItem.objects.filter(product=product, fav=fav).exists()
        if is_fav_item_exists:
            fav_item = favItem.objects.filter(product=product, fav=fav)
            # existing_variations -> database
            # current variation -> product_variation
            # item_id -> database
            ex_var_list = []
            id = []
            for item in fav_item:
                existing_variation = item.variations.all()
                ex_var_list.append(list(existing_variation))
                id.append(item.id)

            print(ex_var_list)

            if product_variation in ex_var_list:
                # increase the fav item quantity
                index = ex_var_list.index(product_variation)
                item_id = id[index]
                item = favItem.objects.get(product=product, id=item_id)
                item.quantity += 1
                item.save()

            else:
                item = favItem.objects.create(product=product, quantity=1, fav=fav)
                if len(product_variation) > 0:
                    item.variations.clear()
                    item.variations.add(*product_variation)
                item.save()
        else:
            fav_item = favItem.objects.create(
                product = product,
                quantity = 1,
                fav = fav,
            )
            if len(product_variation) > 0:
                fav_item.variations.clear()
                fav_item.variations.add(*product_variation)
            fav_item.save()
        return redirect('favourite')


def remove_fav(request, product_id, fav_item_id):

    product = get_object_or_404(Product, id=product_id)
    try:
        if request.user.is_authenticated:
            fav_item = favItem.objects.get(product=product, user=request.user, id=fav_item_id)
        else:
            fav = fav.objects.get(fav_id=_fav_id(request))
            fav_item = favItem.objects.get(product=product, fav=fav, id=fav_item_id)
        if fav_item.quantity > 1:
            fav_item.quantity -= 1
            fav_item.save()
        else:
            fav_item.delete()
    except:
        pass
    return redirect('favourite')


def remove_fav_item(request, product_id, fav_item_id):
    product = get_object_or_404(Product, id=product_id)
    if request.user.is_authenticated:
        fav_item = favItem.objects.get(product=product, user=request.user, id=fav_item_id)
    else:
        fav = fav.objects.get(fav_id=_fav_id(request))
        fav_item = favItem.objects.get(product=product, fav=fav, id=fav_item_id)
    fav_item.delete()
    return redirect('favourite')



def fav(request, total=0, quantity=0, fav_items=None):
    try:
        tax = 0
        grand_total = 0
        if request.user.is_authenticated:
            fav_items = favItem.objects.filter(user=request.user, is_active=True)
        else:
            fav = fav.objects.get(fav_id=_fav_id(request))
            fav_items = favItem.objects.filter(fav=fav, is_active=True)
        for fav_item in fav_items:
            total += (fav_item.product.price * fav_item.quantity)
            quantity += fav_item.quantity
        tax = (2 * total)/100
        grand_total = total + tax
    except ObjectDoesNotExist:
        pass #just ignore

    context = {
        'total': total,
        'quantity': quantity,
        'fav_items': fav_items,
        'tax'       : tax,
        'grand_total': grand_total,
    }
    return render(request, 'store/favourite.html', context)

@login_required(login_url='login')
def checkout(request, total=0, quantity=0, fav_items=None):
    try:
        tax = 0
        grand_total = 0
        if request.user.is_authenticated:
            fav_items = favItem.objects.filter(user=request.user, is_active=True)
        else:
            fav = fav.objects.get(fav_id=_fav_id(request))
            fav_items = favItem.objects.filter(fav=fav, is_active=True)
        for fav_item in fav_items:
            total += (fav_item.product.price * fav_item.quantity)
            quantity += fav_item.quantity
        tax = (2 * total)/100
        grand_total = total + tax
    except ObjectDoesNotExist:
        pass #just ignore

    context = {
        'total': total,
        'quantity': quantity,
        'fav_items': fav_items,
        'tax'       : tax,
        'grand_total': grand_total,
    }
    return render(request, 'store/checkout.html', context)
