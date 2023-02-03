from django.forms import ModelForm, TextInput, EmailInput, HiddenInput
from .models import OrderUser, Product


class OrderForm(ModelForm):
    class Meta:
        model = OrderUser
        fields = ['user_name', 'email', 'product_id']
        widgets = {
            'user_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name'
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            # 'product_id': HiddenInput()
        }
    #
    # def save(self, *args, **kwargs):
    #     self.instance.product_id = '1'
    #     return super(OrderForm, self).save(*args, **kwargs)

    # def form_valid(self, form):
    #     product = Product.objects.get(id=self.kwargs['product_id'])
    #     form.instance.product = product
    #     return super(self).form_valid(form)


    # def save(self, *args, **kwargs):
    #     data = self.cleaned_data
    #     orderuser = OrderUser(user_name=data['user_name'], email=data['email'])
    #     orderuser.save()
    #     orderproduct = Product(product_id=self.product_id)
    #     orderproduct.save()
    #
    # def __init__(self, *args, **kwargs):
    #     self.product_id = Product.product_name
    #     super().__init__(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #     self.instance.product_id = self.product_id
    #     return super().save(*args, **kwargs)