from django.shortcuts import render

# Create your views here.









######### Views for Order model in basket:

# class OrderList(LoginRequiredMixin,SelectRelatedMixin,ListView):
#     model = models.Order
#     select_related = ['account','order']

    # def get_queryset(self):
        # try:
        #     queryset = super().get_queryset(model=Account?) ???
        #     return queryset.filter(customer_id__exact=self.kwargs.get('username'))
        ### ^ Get an account with this specific customer variable

        # except DoesNotExist:
                ## redirect to CreateAccount view.
        #### ^ if an account with this specific customer variable doesn't exist

# class OrderList(TemplateView):
#     template_name = 'accounts/_order_list.html'
#
# class EditSuccess(TemplateView):
#     template_name = 'edit_success.html'
