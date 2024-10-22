import re

class TrieNode:
    def __init__(self, size=63):
        self.link = [None] * size  # 0: $, 1-26: a-z, 27-52: A-Z, 53-62: 0-9
        self.is_end = False  
        self.frequency = 0 
        self.word = None  
        self.char = None  

    def get_index(self, char: str) -> int:
        if char == '$':
            return 0
        elif 'a' <= char <= 'z':
            return ord(char) - ord('a') + 1       # Indices 1-26
        elif 'A' <= char <= 'Z':
            return ord(char) - ord('A') + 27      # Indices 27-52
        elif '0' <= char <= '9':
            return ord(char) - ord('0') + 53      # Indices 53-62
        else:
            return -1  # Invalid character

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            index = current.get_index(char)
            if index == -1:
                continue  # Skip invalid characters
            if current.link[index] is None:
                current.link[index] = TrieNode()
                current.link[index].char = char
            current = current.link[index]
        if current.is_end:
            current.frequency += 1
        else:
            current.is_end = True
            current.frequency = 1
            current.word = word  # Store the word at the end node

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            index = current.get_index(char)
            if index == -1 or current.link[index] is None:
                return False
            current = current.link[index]
        return current.is_end

    def collect_words(self, node, max_words, words_collected):
        """
        Collect words from the Trie starting at the given node.

        Args:
            node (TrieNode): The starting node.
            max_words (int): Maximum number of words to collect.
            words_collected (list): The list to store collected words.
        """
        if node.is_end:
            words_collected.append((node.word, node.frequency))
            if len(words_collected) >= max_words:
                return

        for idx in range(len(node.link)):
            child = node.link[idx]
            if child is not None:
                self.collect_words(child, max_words, words_collected)
                if len(words_collected) >= max_words:
                    return

    @staticmethod
    def common_prefix_length(s1: str, s2: str) -> int:
        length = min(len(s1), len(s2))
        for i in range(length):
            if s1[i] != s2[i]:
                return i
        return length

class SpellChecker:
    """
    The SpellChecker object for checking the spelling of words using a Trie.

    Attributes:
        trie: A Trie object to store the words and their frequencies.
    """
    def __init__(self, filename: str) -> None:
        self.trie = Trie()
        self.build_trie(filename)

    def build_trie(self, filename: str) -> None:
        with open(filename, 'r') as file:
            for line in file:
                words = re.findall(r'[A-Za-z0-9]+', line)
                for word in words:
                    self.trie.insert(word)

    def check(self, input_word: str) -> list:
        if self.trie.search(input_word):
            return []

        suggestions = []
        max_suggestions = 3
        word_length = len(input_word)
        collected_words = []

        # Try prefixes from longest to shortest
        for prefix_length in range(word_length, 0, -1):
            current = self.trie.root
            matched = True
            for i in range(prefix_length):
                char = input_word[i]
                index = current.get_index(char)
                if index == -1 or current.link[index] is None:
                    matched = False
                    break
                current = current.link[index]
            if matched:
                words_from_current_prefix = []
                self.trie.collect_words(current, max_suggestions * 2, words_from_current_prefix)
                for word, freq in words_from_current_prefix:
                    common_prefix_len = self.trie.common_prefix_length(input_word, word)
                    # Only add words that share a non-empty common prefix
                    if common_prefix_len > 0:
                        suggestions.append((common_prefix_len, freq, word))
                # Remove duplicates while preserving order
                unique_suggestions = []
                seen_words = []
                for item in suggestions:
                    if item[2] not in seen_words:
                        seen_words.append(item[2])
                        unique_suggestions.append(item)
                suggestions = unique_suggestions
                if len(suggestions) >= max_suggestions:
                    break  # We have enough suggestions
        if not suggestions:
            return []

        # If still not enough suggestions, try shorter prefixes
        if len(suggestions) < max_suggestions:
            # Try prefixes shorter than the ones we've tried
            for prefix_length in range(prefix_length - 1, 0, -1):
                current = self.trie.root
                matched = True
                for i in range(prefix_length):
                    char = input_word[i]
                    index = current.get_index(char)
                    if index == -1 or current.link[index] is None:
                        matched = False
                        break
                    current = current.link[index]
                if matched:
                    words_from_current_prefix = []
                    self.trie.collect_words(current, max_suggestions * 2, words_from_current_prefix)
                    for word, freq in words_from_current_prefix:
                        common_prefix_len = self.trie.common_prefix_length(input_word, word)
                        if common_prefix_len > 0:
                            suggestions.append((common_prefix_len, freq, word))
                    # Remove duplicates
                    unique_suggestions = []
                    seen_words = [item[2] for item in suggestions[:len(suggestions)-len(words_from_current_prefix)]]
                    for item in suggestions[len(suggestions)-len(words_from_current_prefix):]:
                        if item[2] not in seen_words:
                            seen_words.append(item[2])
                            unique_suggestions.append(item)
                    suggestions = suggestions[:len(suggestions)-len(words_from_current_prefix)] + unique_suggestions
                    if len(suggestions) >= max_suggestions:
                        break  # We have enough suggestions

        # # Sort suggestions according to the ranking
        # suggestions.sort(key=lambda x: (-x[0], -x[1], x[2]))

        # Extract the words
        top_words = [item[2] for item in suggestions[:max_suggestions]]
        return top_words

# Example usage
myChecker = SpellChecker("Messages.txt")

print(myChecker.check("IDK"))   # Expected Output：[]
print(myChecker.check("zoo"))   # Expected Output：[]
print(myChecker.check("LOK"))   # Expected Output：["LOL", "LMK"]
print(myChecker.check("IDP"))   # Expected Output：["IDK", "IDC", "I"]
print(myChecker.check("Ifc"))   # Expected Output：["If", "I", "IDK"]