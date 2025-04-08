from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from products.forms import CommentModelForm
from products.models import ProductModel, BannerModel


class HomeListView(ListView):
    queryset = ProductModel
    template_name = 'index.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['discounts'] = ProductModel.objects.order_by('-discount')[:3]
        context['banners'] = BannerModel.objects.filter(is_active=True)[:3]
        return context


class AboutTemplateView(TemplateView):
    template_name = 'about.html'


class ShopListView(ListView):
    queryset = ProductModel.objects.order_by('-pk')
    template_name = 'shop.html'
    context_object_name = 'products'
    paginate_by = 9

    def get_queryset(self):
        qs = ProductModel.objects.order_by('-pk')

        q = self.request.GET.get('q')

        if q:
            qs = qs.filter(name__icontains=q)

        return qs


class ProductDetailView(DetailView):
    model = ProductModel
    template_name = 'shop-single.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['related'] = self.object.category.products.exclude(pk=self.object.pk)[:4]
        return context


class LoginView(TemplateView):
    template_name = 'login.html'


class RegisterView(TemplateView):
    template_name = 'registration.html'


class CommentCreateView(CreateView):
    form_class = CommentModelForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.product = get_object_or_404(ProductModel, pk=self.kwargs['pk'])

        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('products:detail', kwargs={'pk': self.kwargs['pk']})


class WishlistListView(LoginRequiredMixin, ListView):
    template_name = 'wishlist.html'
    context_object_name = 'products'
    paginate_by = 9

    def get_queryset(self):
        return self.request.user.wishlist.order_by('-pk')


@login_required
def create_wishlist(request, pk):
    product = get_object_or_404(ProductModel, pk=pk)

    if request.user in product.wishlist.all():
        product.wishlist.remove(request.user)

    else:
        product.wishlist.add(request.user)

    product.save()

    return redirect(request.GET.get('next', '/'))


class CartView(TemplateView):
    template_name = 'cart.html'
