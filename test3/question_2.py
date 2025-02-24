def filter_sensitive_words(text, sensitive_words):
    for word in sensitive_words:
        text = text.replace(word, '*')
    return text

raw_text = """
在当今的互联网时代，信息传播的速度之快、范围之广前所未有，但同时也伴随着一些不良信息的传播，其中就包括敏感词汇的使用。
敏感词，通常指的是那些具有争议性、攻击性、侮辱性或者涉及个人隐私、政治敏感等内容的词汇。
这些词汇的使用，往往会对他人造成伤害，引发社会争议，甚至触犯法律法规。
因此，对敏感词进行过滤，是维护网络健康、文明交流的重要措施。通过技术手段对敏感词进行识别和过滤，可以有效净化网络环境，保护用户免受不良信息的侵扰。
同时，我们也应该自觉遵守网络道德规范，不使用敏感词汇，共同营造一个和谐、健康的网络空间。
在这个过程中，技术的进步和公众意识的提升将共同推动网络环境的持续改善。
"""
sensitive_words = ["争议", "侮辱"]
text = filter_sensitive_words(raw_text, sensitive_words)
print(text)
