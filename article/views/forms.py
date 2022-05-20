from django import forms
#引入froms表单
from article.models import ArticlePost
#引入数据库（文章）

class ArticlePostForm(forms.ModelForm):
    class Meta:
        #指定数据模型来源
        model = ArticlePost
        #包含的字段
        fields = ('title','body')