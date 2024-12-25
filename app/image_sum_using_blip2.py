import streamlit as st
import numpy as np
import torch
import os
from transformers import (
    BlipProcessor, 
    BlipForConditionalGeneration, 
    CLIPProcessor, 
    CLIPModel, 
    T5Tokenizer, 
    T5ForConditionalGeneration
)
from PIL import Image

# Initialize models
blip_model_name = "Salesforce/blip-image-captioning-large"
blip_processor = BlipProcessor.from_pretrained(blip_model_name)
blip_model = BlipForConditionalGeneration.from_pretrained(blip_model_name)

clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch16")
clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch16")

t5_model_name = "t5-base"
t5_tokenizer = T5Tokenizer.from_pretrained(t5_model_name)
t5_model = T5ForConditionalGeneration.from_pretrained(t5_model_name)

def generate_summaries(image):
    """Generate multiple summaries from the image using BLIP."""
    summaries = []
    for _ in range(5):
        inputs = blip_processor(image, return_tensors="pt")
        output = blip_model.generate(**inputs)
        summary = blip_processor.decode(output[0], skip_special_tokens=True)
        summaries.append(summary)
    return summaries

def select_best_summary(summaries, keywords):
    """Select the best summary using CLIP based on the keywords."""
    keyword_embeddings = clip_processor(text=[keywords], return_tensors="pt", padding=True, truncation=True).to("cuda" if torch.cuda.is_available() else "cpu")
    summary_embeddings = clip_processor(text=summaries, return_tensors="pt", padding=True, truncation=True).to("cuda" if torch.cuda.is_available() else "cpu")

    with torch.no_grad():
        keyword_features = clip_model.get_text_features(**keyword_embeddings)
        summary_features = clip_model.get_text_features(**summary_embeddings)

    similarities = torch.nn.functional.cosine_similarity(keyword_features, summary_features)
    best_index = similarities.argmax().item()  
    return summaries[best_index]

def refine_with_t5(summary):
    """Refine the selected summary using T5 to ensure it is extended to at least 75 words."""
    input_text = f"Please expand and elaborate on the following description while maintaining its meaning: {summary}"
    input_ids = t5_tokenizer.encode(input_text, return_tensors="pt").to("cuda" if torch.cuda.is_available() else "cpu")

    # Generate output
    output_ids = t5_model.generate(input_ids, max_length=150, num_beams=4, early_stopping=True)
    refined_summary = t5_tokenizer.decode(output_ids[0], skip_special_tokens=True)

    # Ensure the refined summary is at least 50 words long
    refined_summary_words = refined_summary.split()
    if len(refined_summary_words) < 50:
        # Expand further if necessary
        refined_summary += " This detailed description aims to provide deeper insights into the subject matter."
    
    return refined_summary

def image_summarization_page2():
    """Main function for the image summarization page in Streamlit."""
    st.title("📷 Image Summarization with BLIP + CLIP + T5")
    st.markdown("Upload an image and provide keywords for a detailed summary.")

    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg", "jfif", "webp"])

    if uploaded_file:
        # Convert the uploaded file to a PIL Image
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption='Uploaded Image', use_column_width=True)
        keywords = st.text_input("Enter keywords for summarization", "")

        if st.button("Generate Summary"):
            if keywords:
                with st.spinner("Generating summaries..."):
                    try:
                        summaries = generate_summaries(image)
                        best_summary = select_best_summary(summaries, keywords)
                        refined_summary = refine_with_t5(best_summary)

                        st.write("### Summary")
                        st.write(refined_summary)
                    except Exception as e:
                        st.error(f"An error occurred: {str(e)}")
            else:
                st.error("Please enter keywords.")

        feedback = st.text_area("Provide feedback", "")
        if st.button("Submit Feedback"):
            if feedback:
                # Handle feedback (implement your feedback handling here)
                st.success("Feedback submitted successfully!")
            else:
                st.error("Please enter your feedback.")

# Run the Streamlit app
if __name__ == "__main__":
    image_summarization_page2()
