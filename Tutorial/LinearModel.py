from matplotlib import pyplot as plt
import numpy as np
import statistics

# Dati della tabella
data = np.array([[833. ,  37. ],
                 [987. ,  41.6],
                 [883. ,  37.2],
                 [378. ,  15.2],
                 [ 84. ,   3.4],
                 [483. ,  19.6],
                 [835. ,  35.1],
                 [646. ,  28.9],
                 [508. ,  22.6],
                 [ 90. ,   3.7]])

#------------------------
# definizione del modello
#------------------------

class LinearModel:

  def __init__(self) :

    self.angular_coeff = None;
    self.intercept = None;
    self.train_data = None;

  #------------------------------------------------------------------------------------------------

  def fit(self, train_data) :
    # controllo che train_data sia della forma giusta
    try:
      assert(len(train_data.shape)==2)
      assert(train_data.shape[1]==2)
    except:
      raise Exception("Bad train_data shape! {} should be (*,2)".format(train_data.shape))
  
	  # ricavo le x e le y da train_data
    x = train_data[:,0]
    y = train_data[:,1]

    x_media = np.mean(x);
    y_media = np.mean(y);

    self.angular_coeff = np.corrcoef(x, y)[0, 1] * (np.std(y, ddof = 1) / np.std(x, ddof = 1));
    self.intercept = y_media - self.angular_coeff * x_media;
    self.train_data = train_data;

    linear_plot = LinearPlot();
    linear_plot.create_plot(x, y, self.angular_coeff, self.intercept);

  #------------------------------------------------------------------------------------------------

  def predict(self, xs) :

    y_i = [];
  
    for x_i in xs :
      y_i.append((self.angular_coeff * x_i) + self.intercept);

    return y_i[-1];

###################################################################################################

class LinearPlot() : # Creazione del modello grafico.

    def create_plot(self, x, y, m, q) :

      plt.plot(x, y, 'o');
      plt.plot(x, m*x + q);
      plt.show();

###################################################################################################

#-------------------------
# applicazione del modello
#-------------------------

#TODO: istanziare il modello
linear = LinearModel();
#TODO: effetuare il fit
linear.fit(data);

km_tragitto = 2500;
xs = [833, 987, 883, 378, 84, 483, 835, 646, 508, 90, km_tragitto];
#TODO: predire il numero di litri per il tragitto stimato
litri_tragitto = linear.predict(xs);

predict_data = np.array([xs, litri_tragitto]);

prezzo_benzina = 1.4;
#TODO: calcolare la spesa di ciascuno
quota_individuale = (litri_tragitto * prezzo_benzina) / 3;

# Stampa i risultati a schermo
print("\n\nRISULTATI:\n\nLitri di benzina totali: {} lt\nQuota individuale: {} €".format(litri_tragitto,quota_individuale))