from transformers import GPT2LMHeadModel, GPT2Tokenizer


class RugptGenerator:
    def __init__(self):
        self.device = "cpu"  # "cuda" #torch.device("cuda" if torch.cuda.is_available() and not args.no_cuda else "cpu")
        self.tokenizer = None
        self.model = None

    def load(self, model_name_or_path):
        self.device = "cpu"  # "cuda" #torch.device("cuda" if torch.cuda.is_available() and not args.no_cuda else "cpu")
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_name_or_path)
        self.model = GPT2LMHeadModel.from_pretrained(model_name_or_path)
        self.model.to(self.device)

    def generate_output(self, context, num_return_sequences=10):
        temperature = 0.9
        beam_k = 10
        beam_p = 0.9
        repetition_penalty = 1.0
        prompt_text = context + ' #'
        stop_token = "</s>"
        length = 100

        encoded_prompt = self.tokenizer.encode(prompt_text, add_special_tokens=False, return_tensors="pt")
        encoded_prompt = encoded_prompt.to(self.device)

        output_sequences = self.model.generate(
            input_ids=encoded_prompt,
            max_length=length + len(encoded_prompt[0]),
            temperature=temperature,
            top_k=beam_k,
            top_p=beam_p,
            repetition_penalty=repetition_penalty,
            do_sample=True,
            num_return_sequences=num_return_sequences,
            pad_token_id=self.tokenizer.encoder['<pad>']
        )

        # Remove the batch dimension when returning multiple sequences
        if len(output_sequences.shape) > 2:
            output_sequences.squeeze_()

        generated_sequences = set()
        for generated_sequence_idx, generated_sequence in enumerate(output_sequences):
            #print("ruGPT2Large:".format(generated_sequence_idx + 1))
            generated_sequence = generated_sequence.tolist()

            # Decode text
            text = self.tokenizer.decode(generated_sequence, clean_up_tokenization_spaces=True)

            # Remove all text after the stop token
            if stop_token in text:
                text = text[: text.find(stop_token)]

            # Add the prompt at the beginning of the sequence. Remove the excess text that was used for pre-processing
            total_sequence = text[len(self.tokenizer.decode(encoded_prompt[0], clean_up_tokenization_spaces=True)):]

            if '#' in total_sequence:
                total_sequence = total_sequence[: total_sequence.find('#')]

            total_sequence = total_sequence.strip()
            generated_sequences.add(total_sequence)
            #print(total_sequence)

        return list(generated_sequences)
