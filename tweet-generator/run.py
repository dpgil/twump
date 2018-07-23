from textgenrnn import textgenrnn

# textgen = textgenrnn('C:\\Users\\bahariri\\AppData\\Local\\Continuum\\anaconda3\\Lib\\site-packages\\textgenrnn_weights.hdf5')
# textgen.generate(10, temperature=.69)

textgen_2 = textgenrnn('C:\\Users\\bahariri\\Desktop\\workspace\\twump\\tweet-generator\\textgenrnn_weights.hdf5')
textgen_2.generate_samples()