from blog.models import Post
from django.utils.text import slugify
import random
from django.core.management.base import BaseCommand, CommandError
import datetime
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def generate_random_date(self):
        start_date = datetime.date(2020, 1, 1)
        end_date = datetime.date(2021, 8, 14)
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(
            days=random_number_of_days
        )
        return random_date

    def generate_random_tags(self):
        words = [
            "Donec dui massa",
            "tincidunt et luctus sed",
            "convallis in elit",
            "Integer eget tincidunt lectus",
            "Sed in nisi odio",
            "Fusce nulla purus",
            "tincidunt ac nulla non",
            "pellentesque luctus enim",
            "Ut vulputate odio nec ornare faucibus",
            "Donec dignissim commodo nulla vel feugiat",
            "In vel ipsum elitMorbi viverra",
            "Fusce porttitor erat consequat ornare ornare",
        ]
        return words[random.randint(0, len(words) - 1)]

    def generate_random_title(self):
        titles = [
            "Donec dui massa",
            "tincidunt et luctus sed",
            "convallis in elit",
            "Integer eget tincidunt lectus",
            "Sed in nisi odio",
            "Fusce nulla purus",
            "tincidunt ac nulla non",
            "pellentesque luctus enim",
            "Ut vulputate odio nec ornare faucibus",
            "Donec dignissim commodo nulla vel feugiat",
            "In vel ipsum elitMorbi viverra",
            "Fusce porttitor erat consequat ornare ornare",
        ]
        title = titles[random.randint(0, len(titles) - 1)]
        slug = slugify(title, allow_unicode=True)
        return title, slug

    def handle(self, *args, **options):
        user = User.objects.get(pk=1)
        for x in range(50):
            title, slug = self.generate_random_title()
            post = Post(
                title=title,
                slug=slug,
                author=user,
                body="""
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eget magna nec turpis varius volutpat. Duis vitae ligula lacus. Pellentesque facilisis tempus justo porta finibus. Donec augue orci, condimentum id neque sed, vulputate mattis est. Donec in aliquet felis. Phasellus rhoncus libero sed maximus tempor. Etiam at viverra velit, in lacinia neque. Morbi purus tortor, venenatis nec rutrum eget, pretium id tellus.

                Vivamus vehicula velit quam, at fermentum enim vehicula a. Donec pellentesque nunc velit, sit amet sodales odio porttitor vitae. Maecenas quis consectetur ante. Suspendisse potenti. Phasellus blandit fringilla nisi, non tempor lorem tempus sit amet. Aliquam consequat risus sodales nunc condimentum, et malesuada lorem viverra. Vestibulum congue magna quam, et tristique eros molestie vitae. Sed egestas lectus et elementum faucibus. Nam semper arcu nec metus convallis auctor. Mauris eu convallis justo. Ut tempor non justo posuere lobortis.

                Suspendisse eget tellus arcu. Etiam a gravida turpis. Sed laoreet pellentesque elit, sit amet convallis felis porttitor vel. Mauris mauris lectus, lacinia nec malesuada ut, facilisis vel arcu. Nulla facilisi. Integer et placerat risus, ac rhoncus elit. Nullam at tellus sit amet dolor congue blandit ut ut nisi. Integer vitae erat tellus.

                Fusce ut finibus felis. Donec dui massa, tincidunt et luctus sed, convallis in elit. Integer eget tincidunt lectus. Sed in nisi odio. Fusce nulla purus, tincidunt ac nulla non, pellentesque luctus enim. Ut vulputate odio nec ornare faucibus. Donec dignissim commodo nulla vel feugiat. In vel ipsum elit. Morbi viverra, urna a rhoncus sollicitudin, nisi tortor viverra nisl, non lacinia eros metus id ligula. Fusce porttitor erat consequat ornare ornare.

                Phasellus lacus leo, cursus a suscipit et, fringilla sed tortor. Nam porttitor mi id mi faucibus, ut malesuada arcu aliquam. Duis sit amet ornare turpis. Aliquam tincidunt vehicula gravida. Pellentesque ultrices nunc vel viverra semper. Vivamus accumsan scelerisque quam, nec tincidunt nulla ultricies quis. Etiam elit odio, pellentesque id est vel, aliquet dapibus turpis. Sed eget est et lectus sollicitudin rutrum a aliquam turpis. Pellentesque congue, sapien non imperdiet volutpat, elit sapien commodo enim, et lobortis est velit id magna. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Ut non lacus tortor.

                Donec aliquam turpis et urna tristique, at interdum dui pellentesque. Sed malesuada maximus erat, et lacinia dui facilisis ut. Praesent porta mattis vulputate. Donec non turpis cursus felis tristique rhoncus nec a tortor. Aliquam ac nibh mattis, lobortis ex non, porta erat. Cras tempor non tortor ac cursus. Donec arcu massa, pulvinar et magna in, viverra sodales augue. Nullam finibus lacus sed lectus ullamcorper volutpat. Nullam nec arcu a neque molestie sollicitudin. Nam non semper velit, quis ultrices tortor. Curabitur ac neque velit. Aenean venenatis congue justo nec auctor. Curabitur facilisis ante in neque vulputate pretium. In faucibus convallis sodales. Proin et mauris libero.

                Sed faucibus suscipit feugiat. Cras at lectus in purus luctus consequat eu a sem. Aenean eu facilisis est. Etiam dui turpis, bibendum pretium pharetra vel, interdum ut ex. Ut eget nisl lectus. Etiam aliquet urna nec enim pharetra pellentesque. Praesent vel nisl vel enim imperdiet auctor. Nam velit libero, vulputate tempor suscipit ut, malesuada vitae sem. Nulla mattis, purus id cursus vulputate, arcu nisi vestibulum nisl, interdum porttitor enim risus scelerisque lacus. Integer enim sapien, vestibulum et massa ut, dignissim suscipit urna. Morbi pharetra imperdiet purus vel sodales.

                Proin nibh risus, porttitor eu orci eu, ultrices efficitur nibh. Etiam nec scelerisque nisi. Quisque et arcu euismod tellus porta venenatis vel eget tortor. Mauris ultricies libero vel risus dapibus suscipit. Praesent lacinia libero tincidunt varius condimentum. Ut pellentesque erat lorem, ut mollis nisl elementum at. In dapibus metus vel posuere cursus. Ut eleifend tincidunt vulputate. Donec consectetur, tortor et porttitor finibus, massa elit convallis magna, eu lacinia arcu est ac turpis. Cras lorem orci, dictum in augue quis, luctus interdum nibh. Vivamus sit amet neque vitae eros vehicula fermentum at vitae ipsum. In hac habitasse platea dictumst. Aliquam egestas tempor nunc, nec eleifend lectus aliquet non. Suspendisse accumsan pharetra massa, ac vehicula nibh pellentesque sit amet.

                Mauris ac lacus quis leo efficitur malesuada quis in neque. Proin eleifend odio vel mi congue, eu accumsan felis vulputate. Nam sit amet turpis non eros ornare mollis et et ipsum. Nulla interdum ligula urna, sit amet rutrum turpis blandit vel. Proin feugiat tincidunt luctus. Vivamus luctus nisi quis magna dictum pretium. Nunc eu convallis enim.

                Morbi tempor magna a feugiat lacinia. Quisque a felis finibus, consectetur purus a, dictum tellus. Maecenas pretium sodales ante. Sed vel posuere augue. Nunc vestibulum, nibh id porta efficitur, eros turpis viverra ipsum, nec dignissim dui risus vel massa. Maecenas sit amet eros quis ex pharetra posuere. Duis sit amet dictum libero. Duis elit nisi, tempor ut tincidunt ut, vulputate sit amet lacus. Donec augue ex, volutpat eu hendrerit vel, porttitor quis orci. Mauris volutpat iaculis mi. Mauris consectetur elit id rutrum bibendum. Nam quis ipsum lacinia, porta nibh luctus, consequat ipsum.

                Donec molestie aliquet tincidunt. Pellentesque laoreet felis eget tortor pretium, sit amet blandit nibh commodo. Vivamus eu malesuada orci, in varius neque. In lobortis lectus a ligula mattis mollis. Vivamus dolor felis, blandit ac semper eget, tincidunt vel ante. Aenean imperdiet nisi cursus eleifend vestibulum. Integer eu imperdiet metus. Proin non velit ligula. Integer condimentum porta mauris, id efficitur velit semper sit amet.

                Nam condimentum odio turpis, et porttitor sem mattis ut. Nam urna erat, hendrerit nec tortor vel, ornare eleifend augue. Donec gravida pharetra libero eget imperdiet. Nunc eros ipsum, dignissim non tempus id, tempus sed justo. Aenean hendrerit eget mi rhoncus rutrum. Aliquam tristique dapibus fringilla. Ut ultricies tellus arcu, a vehicula lacus vehicula quis. Aenean vehicula sit amet elit eget vehicula. Maecenas eleifend urna metus, ac malesuada leo commodo sit amet. Mauris fringilla massa a risus venenatis luctus. Phasellus risus sem, viverra quis lorem eget, commodo blandit nibh. Nunc sollicitudin mi id ornare molestie. Sed blandit feugiat eros non feugiat. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Donec dapibus, mi non sollicitudin maximus, diam lectus aliquet est, nec vehicula erat nisi id dui.

                Nunc id turpis turpis. Aliquam ac quam eu mauris viverra elementum. Donec quis rutrum nisi. In suscipit nulla non facilisis auctor. Proin commodo odio eu metus lobortis molestie. Pellentesque ornare ligula id urna luctus porttitor. Cras lobortis volutpat mauris non lacinia. In pellentesque placerat lobortis. Morbi eu purus rutrum lacus imperdiet semper a vitae est.

                Vivamus vitae dolor et nisi efficitur suscipit sit amet et urna. Fusce et leo auctor nisl molestie tincidunt eget quis nunc. Donec vel metus faucibus, volutpat turpis vitae, pulvinar dui. Nullam iaculis tincidunt erat, quis fermentum felis efficitur vel. Praesent tristique, dui id imperdiet hendrerit, nunc velit facilisis sapien, malesuada finibus metus velit ut sapien. Nullam viverra justo sit amet dolor venenatis, vel maximus massa elementum. Curabitur ac lobortis nisi, et dapibus augue. Etiam est quam, feugiat volutpat feugiat id, euismod aliquam libero. Donec congue quam nec purus pharetra, quis cursus diam hendrerit. Phasellus in facilisis neque, eget maximus nibh. Duis ac mattis enim. Vivamus imperdiet ipsum est, nec tempus ante ornare vitae.

                Suspendisse potenti. Phasellus non lectus non dolor interdum ultricies. Aliquam nulla ligula, gravida commodo dolor quis, accumsan suscipit risus. Vivamus eget sem sed neque fringilla consequat at eu mi. Proin ultricies, urna sed maximus molestie, lorem velit consequat ex, ac posuere sapien metus et lectus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Morbi magna libero, laoreet id volutpat at, porttitor quis felis.
                """,
                publish=self.generate_random_date(),
                status="Published",
                tags=self.generate_random_tags(),
            )
            post.save()
        self.stdout.write(self.style.SUCCESS("Data has been added"))
