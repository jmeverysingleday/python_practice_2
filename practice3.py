from googletrans import Translator

translator = Translator()

sentence = input("책을 읽으며 인상 깊었던 구절을 적어주세요: ")
# 언어 감지
detected = translator.detect(sentence)

# 언어 감지 결과(언어, 신뢰도) 중 언어만 출력
print(detected.lang)

result_eng = translator.translate(sentence, 'en')
result_jap = translator.translate(sentence, 'ja')

print("============ 번역 결과 ============")
print("\n입력어 - ", detected.lang, ": ", sentence)
print("번역어1 - ", result_eng.dest, ": ", result_eng.text)
print("번역어2 - ", result_jap.dest, ": ", result_jap.text)
print("\n =================================")