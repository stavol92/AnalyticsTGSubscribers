from django.db import models
from django.utils.translation import gettext as _


class BotUser(models.Model):
    '''Chatbot users model'''
    telegram_id = models.PositiveBigIntegerField(_('ID Telegram'), db_index=True,
                                                 unique=True)
    username = models.CharField(_('Username'), max_length=150, blank=True, null=True)
    email = models.EmailField(_('email'), blank=True, null=True)
    first_name = models.CharField(_('First Name'), max_length=150, blank=True, null=True)
    last_name = models.CharField(_('Last Name'), max_length=150, blank=True, null=True)

    def __str__(self):
        return f'{self.telegram_id}: {self.username}'

    class Meta:
        verbose_name = _('Bot User')
        verbose_name_plural = _('Bot Users')


class TelegramChat(models.Model):
    '''Telegram channel or chat'''
    bot_user = models.ForeignKey(BotUser, verbose_name=_('Bot User'), on_delete=models.CASCADE)
    name = models.CharField(_('Channel name'), max_length=150, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('Channel chat')
        verbose_name_plural = _('Channels chats')


class InviteLink(models.Model):
    '''Invite link model'''
    telegram_chat = models.ForeignKey(TelegramChat, verbose_name=_('Channel chat'), on_delete=models.CASCADE)
    creates_join_request = models.BooleanField(_('Request to add'), default=False)
    creator = models.CharField(_('Creator'), max_length=250, blank=True, null=True)
    expire_date = models.CharField(_('Expire date'), max_length=150, blank=True, null=True)
    member_limit = models.CharField(_('Member limit'), max_length=150, blank=True, null=True)
    link = models.CharField(_('Invite link'), max_length=150, blank=True, null=True)
    is_primary = models.CharField(_('Is primary'), max_length=150, blank=True, null=True)
    is_revoked = models.BooleanField(_('Is revoked'), blank=True, null=True)
    member_limit = models.IntegerField(_('Subscription limit'), blank=True, null=True)
    link_name = models.CharField(_('Link name'), max_length=150, blank=True, null=True)
    pending_join_request_count = models.CharField(_('Pending join request count'), max_length=150, blank=True,
                                                  null=True)

    def __str__(self):
        return f'{self.link}'

    class Meta:
        verbose_name = _('Invite link')
        verbose_name_plural = _('Invite links')


class TelegramSubscriber(models.Model):
    '''Channel users model'''
    invite_link = models.ForeignKey(InviteLink, verbose_name=_('Invite link'), on_delete=models.CASCADE)
    telegram_id = models.PositiveBigIntegerField(_('ID Telegram'), db_index=True, unique=True)
    username = models.CharField(_('Username'), max_length=150, blank=True, null=True)
    email = models.EmailField(_('email'), blank=True, null=True)
    first_name = models.CharField(_('First Name'), max_length=150, blank=True, null=True)
    last_name = models.CharField(_('Last Name'), max_length=150, blank=True, null=True)
    subscribed = models.BooleanField(_('Subscribed'), default=False)
    datetime_subscribe = models.DateTimeField(_('Subscription date'), blank=True, null=True)
    datetime_unsubscribe = models.DateTimeField(_('Unsubscription date'), blank=True, null=True)

    def __str__(self):
        return f'{self.telegram_id}: {self.username}'

    class Meta:
        verbose_name = _('Subscriber')
        verbose_name_plural = _('Subscribers')
