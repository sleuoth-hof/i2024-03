from models.newsModel  import  NewsEvaluation
def run_strategy():
    news_evaluations = NewsEvaluation.objects.all()

    for evaluation in news_evaluations:
        confidence = evaluation.confidence
        advice = evaluation.advice
        news_date = evaluation.news_date  

        if confidence >= 40:  
            if advice == 'Buy':
                print("Buy on", news_date)
            elif advice == 'Sell':
                print("Sell on ", news_date)

run_strategy()