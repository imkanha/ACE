from django.shortcuts import render, redirect, HttpResponse
from .forms import ContactForm

def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Your form submitted successfully</h1>")
        
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def index(request):
    return render(request, 'index.html')

def electricbike(request):
    return render(request, 'electricbike.html')

def electricboat(request):
    return render(request, 'electricboat.html')

def drone(request):
    return render(request,'drone.html')

def cybersecurity(request):
    return render(request, 'cybersecurity.html')

def supplychain(request):
    return render(request, 'supplychain.html')

def exammanagement(request):
    return render(request, 'exammanagement.html')

def assessment(request):
    return render(request, 'assessment.html')

def globaleducation(request):
    return render(request, 'globaleducation.html')

def realestate(request):
    return render(request, 'realestate.html')

def company_history(request):
    return render(request, 'company-history.html')

def groupcompany(request):
    return render(request, 'groupcompany.html')

def client(request):
    return render(request, 'client.html')

def socialinitiatives(request):
    return render(request, 'socialinitiatives.html')

def financial_result(request):
    return render(request, 'financial-result.html')

def financial_statement(request):
    return render(request, 'financial-statement.html')

def annual_report(request):
    return render(request, 'annual-report.html')

def otherpublication(request):
    return render(request, 'otherpublication.html')

def boardofdirector(request):
    return render(request, 'boardofdirector.html')

def Composition_of_various_Committees_of_BOD(request):
    return render(request, 'Composition-of-various-Committees-of-BOD.html')

def board_meeting(request):
    return render(request, 'board-meeting.html')

def Disclosures_under_Regulation(request):
    return render(request, 'Disclosures-under-Regulation.html')

def shareholding_pattern(request):
    return render(request, 'shareholding-pattern.html')

def corporate_governance(request):
    return render(request, 'corporate-governance.html')

def stock_exchange(request):
    return render(request, 'stock-exchange.html')

def Disclosures_under_Regulation(request):
    return render(request, 'Disclosures-under-Regulation.html')

def agmegm(request):
    return render(request, 'agmegm.html')

def postal_ballot(request):
    return render(request, 'postal-ballot.html')

def annual_return(request):
    return render(request, 'annual-return.html')

def policies(request):
    return render(request, 'policies.html')

def Investor_Grievances_Cell(request):
    return render(request, 'Investor-Grievances-Cell.html')

def ipo(request):
    return render(request, 'ipo.html')

def ev(request):
    return render(request, 'ev.html')

def mechanical_engineering(request):
    return render(request, 'mechanical-engineering.html')

def agricultural_processing(request):
    return render(request, 'agricultural-processing.html')

def petrolium(request):
    return render(request, 'petrolium.html')

def material_engineering(request):
    return render(request, 'material-engineering.html')

def coachingforemployment(request):
    return render(request,'coachingforemployment.html')

def cybersecurity(request):
    return render(request, 'cybersecurity.html')