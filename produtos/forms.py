from django.forms import ModelForm
from .models import Produto


class ProdForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['nome_produto', 'marca_produto', 'descricao', 'preco', 'foto']
