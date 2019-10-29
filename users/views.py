from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, mixins, permissions, response
#from menu.common import get_menu_tree
from rest_framework.response import Response



class UserInfoViewset(viewsets.ViewSet):
    """
    获取当前登陆的用户信息
    """
    def list(self, request, *args, **kwargs):
        data = {
            "roles": ['admin'],
            "introduction": 'I am a super administrator',
            "avatar": 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
            "name": 'Super Admin'
          }
        ret = {
            "code": 20000,
            "data": data
        }
        return response.Response(ret)



class TokenViewset(viewsets.ViewSet):
    """
    获取当前登陆的用户信息
    """
  #  permission_classes = (permissions.IsAuthenticated,)
    def create(self, request, *args, **kwargs):
        data = {
            "token": 'admin-token'
        }
        ret = {
            "code": 20000,
            "data": data
        }
        return response.Response(ret)

class UsersViewset(viewsets.ViewSet):
    """
    获取当前登陆的用户信息
    """
  #  permission_classes = (permissions.IsAuthenticated,)
    def list(self, request, *args, **kwargs):
        data = {
            "roles": ['admin'],
            "introduction": 'I am a super administrator',
            "avatar": 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
            "name": 'Super Admin'
          #  "menus": get_menu_tree(self.request.user.get_view_permissions())
        }
        return Response(data)
