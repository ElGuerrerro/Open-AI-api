import openai

openai.api_key = 'sk-blablabla'

# intro
Welcome = print("Welcome, I am your  digital music assistant")

# instructions
instrctns = print('I am a playlist creator, you tell me a song you like and I will recommend 10 songs for your new playlist')

# creating the seed song
song = input('What is the name of the song? ')
artiste = input('What artiste(s) own this song? ')
seed_song = (song + ' by ' + artiste)

# sending song to GPT
recommend = ('Recommend ten songs similar to ' + seed_song)
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a chatbot"},
            {"role": "user", "content": recommend}])

print(response['choices'][0]['message']['content'])
