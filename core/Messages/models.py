# from django.db import models

# #Modelos para mensajes 
# from django.contrib.auth import get_user_model

# User = get_user_model()

# #Modelo hilo de usuario,mensaje
# class Thread(models.Model):
#     user = models.ManyToManyField(User, related_name='threads')


# #Modelo hilo de usuarios 
# class Message(models.Model):
#     thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     content = models.TextField()
#     created = models.DateTimeField(auto_now_add=True)


# #Modelo hilo de usuarios 
# class Message(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     content = models.TextField()
#     created = models.DateField(auto_now_add=True)

#     class Meta:
#         ordering = ['created']



# #Modelo hilo de usuario,mensaje
# class Thread(models.Model):
#     user = models.ManyToManyField(User, related_name='threads')
#     messages = models.ManyToManyField(Message)