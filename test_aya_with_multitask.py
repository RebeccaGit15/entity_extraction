from llama_cpp import Llama
from gliner import GLiNER

model = Llama(model_path="SILMA-Streamlit/models/aya-23-8B-Q5_K_M.gguf")

def translate_and_save_arabic_text(text, model, output_file, max_tokens=1024):
    def process_arabic_text_with_end_marker(text, model, max_tokens):
        prompt = f"""
        Please provide only the clean English translation for the following Arabic text. After completing the translation, write 'END_TRANSLATION' to indicate the end of the translation. Do not include any metadata, document details, or extra information.
        
        Text: {text}
        
        Clean Translation:
        """

        result = model(prompt, max_tokens=max_tokens)
        translated_text = result['choices'][0]['text'].strip()

        if 'END_TRANSLATION' in translated_text:
            translated_text = translated_text.split('END_TRANSLATION')[0].strip()

        return translated_text

    final_translation = process_arabic_text_with_end_marker(text, model, max_tokens)

    print("Final clean translation:", final_translation)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(final_translation)

    print(f"Output saved to {output_file}")
    
    return final_translation

text = """
استنادا للأمر الشفهي لمدير عمليات قيادة الجيش و نفيدكم أنه بتاريخه الساعه 18:15 وبالتنسيق مع مديرية المخابرات أرسلت دورية معززة من ل.م.12 الى بلدة كوشا/عكار وعملت على مداهمة عدد من المنازل لاشخاص مطلوبين عل الشكل التالي :
1- المطلوب خالد الزين والدته حنان مواليد 1991 رقم السجل 84 كوشا حيث تم توقيفه كونه مطلوب بموجب وثيقة إطلاق نار ومطلوب بعدة وثائق أعمال ارهابية واطلاق نار وقذائف ار بي جي اخرها الوثيقة رقم 6 تاريخ 14/4/2014.
2- المطلوب ----- والدته ----- مواليد ---- رقم السجل ----.
3- المطلوب ----- والدته ----- مواليد ---- رقم السجل ----.
4- المطلوب ----- والدته ----- مواليد ---- رقم السجل ----.
5- المواطن ------ والدته ----- مواليد ---- رقم السجل ----.
تم العثور على مضبوطات مذكور بالائحة المرفقة ربطا بالوثيقة. كما تمت مداهمة مبنى عائدة للمطلوب خالد الزين (المذكور أعلاه) يستأجره عدد من السوريين حيث اوقف داخل المبنى كل من :
1- السوري ------ والدته ------ مواليد ----.
2- السوري ------ والدته ------ مواليد ----.
3- السوري ------ والدته ------ مواليد ----.
لدخولهم الاراضي البنانية خلسة.
سلم الموقوفين مع أغراضهم الخاصة والمضبوطات الى الشرطة العسكرية باستثناء رمانة يدوية سلمت الى سرية الهندسة ليصار اجراء الازم بشأنها لاحقا.
"""

output_file_path = "results_aya_with_mutlitask/توقيفات_translation.txt"

final_translation = translate_and_save_arabic_text(text, model, output_file_path)


gliner_model = GLiNER.from_pretrained("knowledgator/gliner-multitask-large-v0.5")

def extract_relationships(labels, gliner_model, final_translation, output_file):
    output_lines = []
    
    for label in labels:
        entities = gliner_model.predict_entities(final_translation, [label])
        for entity in entities:
            print(f"{label} => {entity['text']}")
            output_lines.append(f"{label} => {entity['text']}")
    
    with open(output_file, "w", encoding="utf-8") as file:
        for line in output_lines:
            file.write(line + "\n")
    
    print(f"Relationship extraction results saved to {output_file}")

labels = [
    "Khaled el Zein <> mother"
]
re_output_file = "results_aya_with_mutlitask/توقيفات.txt"

extract_relationships(labels, gliner_model, final_translation, re_output_file)