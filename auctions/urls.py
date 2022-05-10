from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_listing", views.new_listing, name="new_listing"),
    path("new_bid/<int:item_id>", views.new_bid, name="new_bid"),
    path("validator_test/<int:item_id>", views.test_form, name="test_form"),
    path("item/<int:item_id>", views.item_page, name="item"),
    path("create_profile/<int:user_id>", views.create_profile, name="create_profile"),
    path("profile/<int:user_id>", views.profile, name="profile"),
    path("new_profile_comment/<int:profile_id>", views.new_comment, name="new_profile_comment"),
    path("new_item_comment/<int:item_id>", views.new_comment, name="new_item_comment"),
    path("close_item/<int:item_id>", views.close_item, name="close_item"),
    path("watch/<int:item_id>", views.watch, name="watch"),
    path("unwatch/<int:item_id>", views.unwatch, name="unwatch"),
    path("watching", views.watchlist, name="watching"),
    path("category_index", views.category_index, name = "category_index"),
    path("category/<int:category_id>", views.category, name="category")
]
"""path("new_bid", views.new_bid, name="new_bid")"""