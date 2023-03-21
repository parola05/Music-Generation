import data_collection as dt
import helpers as hp

keywords = ['RNN', 'Recurrent Neural Network', 'VAE', 'Variational Autoencoder', 'GAN', 'Generative Adversarial Network',
                 'Transformer-based', 'Tranformer', 'Neural Autoregressive', 'NAM', 'Deep Belief Network', 'DBN',
                 'Markov Chain Monte Carlo', 'MCMC', 'Boltzmann Machines', 'BM', 'Hopfield Network']

dt.generateDataCollection(keywords,"Results/architectures_extraction.json")
hp.getNumberOfEachKeywords('Results/architectures_extraction.json', 'Results/architectures_extraction(2).json', keywords)