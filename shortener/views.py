from django.shortcuts import render, get_object_or_404, redirect
from .forms import UrlForm
from .models import Url
import hashLib
# Create your views here.
# Create a base62 encoding function
def base62_encode(num, alphabet=string.ascii_letters + string.digits):
    """Encode a number in Base62 with custom alphabet."""
    if num == 0:
        return alphabet[0]
    arr = []
    base = len(alphabet)
    while num:
        num, rem = divmod(num, base)
        arr.append(alphabet[rem])
    arr.reverse()
    return ''.join(arr)

def index(request):
    if request.method =='POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            long_url = form.cleaned_data['long_url']
            url = Url(long_url=long_url) # create Url instance but don't save it yet
            url.save() # save it to get an id

            # generate a short code and check for collisions
            collision = True
            while collision:
                short_code = base62_encode(url.id) + ''.join(random.choices(string.ascii_uppercase + string.digits, k=4)) # append 4 random alphanumeric characters
                collision = Url.objects.filter(short_code=short_code).exists()

            url.short_code = short_code # assign short_code to url instance
            url.save() # save the instance again
            context = {'url':url}
            return render(request, 'index.html', {'form': form, 'short_code': short_code})
    else:
        form = UrlForm()
    return render(request, 'index.html', {'form': form})

def redirect(request, short_code):
    url = get_object_or_404(Url, short_code=short_code)
    return redirect(url.long_url)