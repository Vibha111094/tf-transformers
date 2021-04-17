import tensorflow as tf
from tf_transformers.utils import get_config
from tf_transformers.core import ModelWrapper
from tf_transformers.models.bert import BERTEncoder
from tf_transformers.models.bert.convert import convert_bert_tf, convert_bert_pt


config = {
    "attention_probs_dropout_prob": 0.1,
    "hidden_act": "gelu",
    "intermediate_act": "gelu",
    "hidden_dropout_prob": 0.1,
    "embedding_size": 768,
    "initializer_range": 0.02,
    "intermediate_size": 3072,
    "max_position_embeddings": 512,
    "num_attention_heads": 12,
    "attention_head_size": 64,
    "num_hidden_layers": 12,
    "type_vocab_size": 2,
    "vocab_size": 28996,
    "layer_norm_epsilon": 1e-12,
    "mask_mode": "user_defined",
}


def normalize_model_name(model_name):
    return model_name.lower().replace("-", "_").strip()


def update_config(tft_config, hf_config):
    """Update tft config with hf config.

    Args:
        tft_config ([type]): [description]
        hf_config ([type]): [description]
    """

    tft_config["vocab_size"] = hf_config["vocab_size"]
    tft_config["embedding_size"] = hf_config["hidden_size"]
    tft_config["intermediate_size"] = hf_config["intermediate_size"]
    tft_config["type_vocab_size"] = hf_config["type_vocab_size"]
    tft_config["max_position_embeddings"] = hf_config["max_position_embeddings"]

    tft_config["num_attention_heads"] = hf_config["num_attention_heads"]
    tft_config["num_hidden_layers"] = hf_config["num_hidden_layers"]

    if "attention_head_size" in tft_config:
        tft_config["attention_head_size"] = tft_config["embedding_size"] // tft_config["num_attention_heads"]
    return tft_config


class BertModel(ModelWrapper):
    def __init__(self, model_name, cache_dir):
        super(BertModel, self).__init__(cache_dir=cache_dir, model_name=model_name)

    @classmethod
    def get_model(
        cls, model_name, cache_dir=None, model_checkpoint_dir=None, convert_from_hf=True, return_layer=False, **kwargs
    ):

        module_name = "tf_transformers.models.model_configs.bert"
        tft_model_name = normalize_model_name(model_name)

        try:
            config = get_config(module_name, tft_model_name)
        except:
            # Load a base config and then overwrite it
            config = get_config(module_name, "bert_base_uncased")
            from transformers import PretrainedConfig

            hf_config = PretrainedConfig.from_pretrained(model_name)
            hf_config = hf_config.to_dict()
            config = update_config(config, hf_config)

        cls_ref = cls(model_name, cache_dir)
        # if we allow names other than
        # whats in the class, we might not be able
        # to convert from hf properly.
        if "name" in kwargs:
            del kwargs["name"]

        tf.keras.backend.clear_session()
        model_layer = BERTEncoder(config, **kwargs)
        model = model_layer.get_model()

        # Give preference to model_checkpoint_dir
        if model_checkpoint_dir:
            model.load_checkpoint(model_checkpoint_dir)
        else:
            load_succesfuly = False
            if cls_ref.model_path.exists():
                try:
                    model.load_checkpoint(str(cls_ref.model_path))
                    load_succesfuly = True
                except:
                    pass
            if convert_from_hf and not load_succesfuly:
                cls_ref.convert_hf_to_tf(
                    model, convert_tf_fn=convert_bert_tf(model, config), convert_pt_fn=convert_bert_pt(model, config)
                )
        if return_layer:
            return model_layer, config
        return model, config
