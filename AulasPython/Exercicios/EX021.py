# Faça um programa em pytjon que abra e reproduza o audio de um arquivo mp3
import pygame

pygame.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()
pygame.event.wait()




