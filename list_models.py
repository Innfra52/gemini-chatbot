import google.generativeai as genai

genai.configure(api_key="AIzaSyBBNX-CD-gH74vEFM2toa1YIDp5w_RFeGg")

print("Available Models:")
for m in genai.list_models():
  # Only show models that support text generation
  if 'generateContent' in m.supported_generation_methods:
    print(f"  - {m.name}")