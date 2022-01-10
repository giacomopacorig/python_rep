# Create il vostro primo modello 
# come abbozzato nella slide precedente!
# Ricordatevi di chiedervi che input possono arrivare e come controllare che 
# siano corretti, e che se volete potete anche scrivere un paio di test

import matplotlib as plt
from matplotlib import pyplot as pllt
from matplotlib import  pyplot

class Model() : # I metodi fit() e predict() non vengono implementati nella classe base.

    def fit(self, data) : # Fit del modello (= farlo aderire ai dati, sfruttare i dati per farlo aderire meglio al fenomeno analizzato).
        pass;

    #----------------------------------------------------------------------------------------------

    def predict(self, data) : # Previsioni
        pass;

###################################################################################################
    
class IncrementModel(Model) : # Implementa il metodo predict() ereditato dalla classe base Model().

    def __str__(self) : 
        return "IncrementModel";

    #----------------------------------------------------------------------------------------------

    def compute_avg_increment(self, data) :
        # Inizializzazione variabili per la raccolta dati settate a None e 0.
        prev_item = None;
        increments = 0;

        for item in data :

            if prev_item is not None : # Se le variabili sono nulle (primo giro della predizione) non esegue il calcolo.
                increments += item - prev_item;

            prev_item = item; # Incremento dell'item precedente.

        avg_increment = increments / (len(data) - 1); # Calcolo finale dell'incremento medio.

        return avg_increment;

    #----------------------------------------------------------------------------------------------

    def predict(self, predict_data) : # Logica per la predizione, ottiene in input una lista di valori di dati noti (in questo caso vendite dei mesi passati).
        
        avg_increment = self.compute_avg_increment(predict_data); # Richiamo del metodo compute_avg_increment().

        return predict_data[-1] + avg_increment; # Incremento medio sommato all'ultimo valore.

###################################################################################################    

class FitIncrementModel(IncrementModel) : # Implementa il metodo fit().

    def __str__(self) :

        return 'FitIncrementModel';

    #----------------------------------------------------------------------------------------------

    def fit(self, fit_data) : # Calcolo dell'incremento medio e salvataggio su una variabile.

        self.global_avg_increment = self.compute_avg_increment(fit_data);

    #----------------------------------------------------------------------------------------------

    def predict(self, predict_data) : # Sovrascrizione del metodo predict() per fargli usare l'incremento medio su tutto il dataset.

        parent_prediction = super().predict(predict_data); # Richiamo del metodo della classe genitore.

        parent_predict_increment = parent_prediction - predict_data[-1]; # Predizione del genitore - ultimo valore predizione = incremento originale.

        prediction_increment = (self.global_avg_increment + parent_predict_increment) / 2; # Media tra incremento fit e predict.

        prediction = predict_data[-1] + prediction_increment; # Somma della media all'ultimo elemento.

        return prediction;

###################################################################################################

class Plot() : # Creazione del modello grafico.

    def create_plot(self, shampoo_sales, predictions) :

        pyplot.plot(shampoo_sales[0 : cutoff_month] + predictions, color = 'tab:red')
        pyplot.plot(shampoo_sales, color = 'tab:blue')
        pyplot.show();

###################################################################################################

# ------ #
## Main ##
# ------ #

# Dati di esempio.
test_fit_data = [8,19,31,41];
test_predict_data = [50,52,60];
shampoo_sales = [266.0, 145.9, 183.1, 119.3, 180.3, 168.5, 231.8, 224.5, 192.8, 122.9, 336.5, 185.9, 194.3, 149.5, 210.1, 273.3, 191.4, 287.0, 226.0, 303.6, 289.9, 421.6, 264.5, 342.3, 339.7, 440.4, 315.9, 439.3, 401.3, 437.4, 575.5, 407.6, 682.0, 475.3, 581.3, 646.9];
eval_months = 12;
cutoff_month = len(shampoo_sales) - eval_months;

# Oggetti.
increment_model = IncrementModel();
fit_increment_model = FitIncrementModel();
plot = Plot();

# Inizio.
fit_increment_model.fit(shampoo_sales[0:cutoff_month]); # Fit sui dati fino al mese di cutoff.
models = [increment_model, fit_increment_model]; # Creazione lista con entrambi i modelli.

for model in models : # Valutazione dei modelli.
    
    error = 0; # Variabile per il calcolo dell'errore.

    print('Evaluating model "{}"'.format(model));
    predictions = [];

    for i in range(eval_months) : # Predizione sulle vendite dello shampoo dal cutoff in poi.

        predict_data = shampoo_sales[cutoff_month+i-3-1:cutoff_month+i-1]
        prediction = model.predict(predict_data);
        real = shampoo_sales[cutoff_month + i]
        print('"{}" (pred) vs "{}" (real)'.format(int(prediction), int(real)))

        # Aggiungo se volessi poi plottare
        predictions.append(prediction)

        error += abs(prediction - shampoo_sales[cutoff_month+i])
    
    error = error / eval_months

    print('Average error: "{}"\n'.format(error))

plot.create_plot(shampoo_sales, predictions);

