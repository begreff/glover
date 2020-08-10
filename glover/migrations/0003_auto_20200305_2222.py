# Generated by Django 2.2.4 on 2020-03-05 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glover', '0002_profile_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='username',
        ),
        migrations.AlterField(
            model_name='course',
            name='course',
            field=models.CharField(choices=[('Accounting', 'Accounting'), ('Anatomy', 'Anatomy'), ('Archaeology', 'Archaeology'), ('Astronomy', 'Astronomy'), ('Biochemistry', 'Biochemistry'), ('Business', 'Business'), ('Celtic Studies', 'Celtic Studies'), ('Chemistry', 'Chemistry'), ('Civil Engineering', 'Civil Engineering'), ('Computing Science', 'Computing Science'), ('Dentistry', 'Dentistry'), ('Earth Science', 'Earth Science'), ('Economics', 'Economics'), ('Engineering', 'Engineering'), ('English Literature', 'English Literature'), ('Film and Television Studies', 'Film and Television Studies'), ('Finance', 'Finance'), ('French', 'French'), ('Gaelic', 'Gaelic'), ('Genetics', 'Genetics'), ('Geography', 'Geography'), ('Geology', 'Geology'), ('German', 'German'), ('Greek', 'Greek'), ('History', 'History'), ('History of Art', 'History of Art'), ('Human Biology', 'Human Biology'), ('Immunology', 'Immunology'), ('Italian', 'Italian'), ('Latin', 'Latin'), ('Marine Biology', 'Marine Biology'), ('Mathematics', 'Mathematics'), ('Medicine', 'Medicine'), ('Microbiology', 'Microbiology'), ('Music', 'Music'), ('Neuroscience', 'Neuroscience'), ('Nursing', 'Nursing'), ('Pharmacology', 'Pharmacology'), ('Philosophy', 'Philosophy'), ('Physics', 'Physics'), ('Physiology', 'Physiology'), ('Politics', 'Politics'), ('Portuguese', 'Portuguese'), ('Psychology', 'Psychology'), ('Russian', 'Russian'), ('Sociology', 'Sociology'), ('Software Engineering', 'Software Engineering'), ('Spanish', 'Spanish'), ('Statistics', 'Statistics'), ('Theology', 'Theology'), ('Veterinary Medicine', 'Veterinary Medicine'), ('Zoology', 'Zoology')], max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='interest',
            name='interest',
            field=models.CharField(choices=[('Yoga', 'Yoga'), ('Football', 'Football'), ('Tennis', 'Tennis'), ('Art', 'Art'), ('Photography', 'Photography'), ('Swimming', 'Swimming'), ('Acting', 'Acting'), ('Animation', 'Animation'), ('Baking', 'Baking'), ('Blogging', 'Blogging'), ('Bowling', 'Bowling'), ('Car Fixing', 'Car Fixing'), ('Cars', 'Cars'), ('Cheesemaking', 'Cheesemaking'), ('Stamp Collecting', 'Stamp Collecting'), ('Programming', 'Programming'), ('Cooking', 'Cooking'), ('Craft', 'Craft'), ('Dance', 'Dance'), ('Drawing', 'Drawing'), ('Painting', 'Painting'), ('Fashion', 'Fashion'), ('Flower Arranging', 'Flower Arranging'), ('Languages', 'Languages'), ('Gaming', 'Gaming'), ('Hacking', 'Hacking'), ('Karaoke', 'Karaoke'), ('Knitting', 'Knitting'), ('Music', 'Music'), ('Films', 'Films'), ('Makeup', 'Makeup'), ('Podcasts', 'Podcasts'), ('Pottery', 'Pottery'), ('Rapping', 'Rapping'), ('Soapmaking', 'Soapmaking'), ('Video Editing', 'Video Editing'), ('Writing', 'Writing'), ('Poetry', 'Poetry'), ('Sports', 'Sports'), ('Gym', 'Gym'), ('Birdwatching', 'Birdwatching'), ('Bodybuilding', 'Bodybuilding'), ('Camping', 'Camping'), ('Canoeing', 'Canoeing'), ('Cycling', 'Cycling'), ('Travel', 'Travel'), ('Graffiti', 'Graffiti'), ('Hiking', 'Hiking'), ('Horseback Riding', 'Horseback Riding'), ('Hunting', 'Hunting'), ('Martial Arts', 'Martial Arts'), ('Parkour', 'Parkour'), ('Scuba Diving', 'Scuba Diving'), ('Shopping', 'Shopping'), ('Skateboarding', 'Skateboarding'), ('Skiing', 'Skiing'), ('Skydiving', 'Skydiving'), ('Survivalism', 'Survivalism'), ('Farming', 'Farming'), ('Knife Collecting', 'Knife Collecting'), ('Boxing', 'Boxing'), ('Food', 'Food'), ('Eating', 'Eating'), ('Debate', 'Debate'), ('Poker', 'Poker'), ('Fishing', 'Fishing'), ('Meditation', 'Meditation'), ('Reading', 'Reading'), ('Learning', 'Learning'), ('People Watching', 'People Watching'), ('Gardening', 'Gardening'), ('Animal Care', 'Animal Care'), ('Singing', 'Singing'), ('Jewelry Making', 'Jewelry Making'), ('Social Media', 'Social Media'), ('Instagram', 'Instagram'), ('Twitter', 'Twitter'), ('Youtube', 'Youtube'), ('TikTok', 'TikTok'), ('Golf', 'Golf'), ('Health and Fitness', 'Health and Fitness'), ('Wine Tasting', 'Wine Tasting'), ('Pet Training', 'Pet Training'), ('Partying', 'Partying'), ('Hosting Parties', 'Hosting Parties'), ('Alcohol', 'Alcohol'), ('Cannabis', 'Cannabis'), ('Extreme Sports', 'Extreme Sports'), ('Social Work', 'Social Work'), ('Nail Art', 'Nail Art'), ('Interior Design', 'Interior Design'), ('Diet and Nutrition', 'Diet and Nutrition'), ('Sculpture', 'Sculpture'), ('Astrology', 'Astrology'), ('Tarot Card Reading', 'Tarot Card Reading'), ('Candle Making', 'Candle Making'), ('Comic Books', 'Comic Books'), ('Volunteering', 'Volunteering'), ('Vegan', 'Vegan'), ('Politics', 'Politics'), ('Environment', 'Environment'), ('Animals', 'Animals')], max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='year_in',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='society',
            name='society',
            field=models.CharField(choices=[('Acapella', 'Acapella'), ('Art and Life Drawing', 'Art and Life Drawing'), ('Art Appreciation', 'Art Appreciation'), ('Astrology', 'Astrology'), ('Astronomy', 'Astronomy'), ('Bad Movie', 'Bad Movie'), ('Baking', 'Baking'), ('Ballroom and Latin Dancing', 'Ballroom and Latin Dancing'), ('Beekeeping', 'Beekeeping'), ('Bhakti Yoga', 'Bhakti Yoga'), ('Big Band', 'Big Band'), ('Bridging Education', 'Bridging Education'), ('Buddhist', 'Buddhist'), ('Business Club', 'Business Club'), ('Food and Body Positivity', 'Food and Body Positivity'), ('Friends of BHF', 'Friends of BHF'), ('Cardiovascular', 'Cardiovascular'), ('Catholic Association', 'Catholic Association'), ('Cecilian', 'Cecilian'), ('Chicken Wing', 'Chicken Wing'), ('Chinese Students Community', 'Chinese Students Community'), ('Chocolate', 'Chocolate'), ('Christian Union', 'Christian Union'), ('Comic Creators Club', 'Comic Creators Club'), ('Communist', 'Communist'), ('Competitive Programming', 'Competitive Programming'), ('Crafts', 'Crafts'), ('Glagow Students for Choice', 'Glagow Students for Choice'), ('Open Cages', 'Open Cages'), ('Scottish Country Dance Club', 'Scottish Country Dance Club'), ('Students Against Climate Change', 'Students Against Climate Change'), ('Dance4Water Glasgow', 'Dance4Water Glasgow'), ('Dancemania', 'Dancemania'), ('Disney', 'Disney'), ('Doctor Who', 'Doctor Who'), ('Documentary', 'Documentary'), ('Drag', 'Drag'), ('Pole Dancing Club', 'Pole Dancing Club'), ('Student Dance Company', 'Student Dance Company'), ('Self Defence', 'Self Defence'), ('European', 'European'), ('Eurovision', 'Eurovision'), ('Exploration', 'Exploration'), ('Extinction Rebellion', 'Extinction Rebellion'), ('Film', 'Film'), ('War Film', 'War Film'), ('Gaming', 'Gaming'), ('Gin', 'Gin'), ('Glasgow Insight into Science and Technology', 'Glasgow Insight into Science and Technology'), ('Game Design and Development', 'Game Design and Development'), ('Scottish Greens', 'Scottish Greens'), ('Glasgow Insight into Science and Technology', 'Glasgow Insight into Science and Technology'), ('Harm Reduction', 'Harm Reduction'), ('Harry Potter', 'Harry Potter'), ('History', 'History'), ('Japan', 'Japan'), ('Jewish', 'Jewish'), ('Juggling at GU', 'Juggling at GU'), ('Students of a Jane Austen Persuasion', 'Students of a Jane Austen Persuasion'), ('K-Pop', 'K-Pop'), ('Korean', 'Korean'), ('GULGBTQ+', 'GULGBTQ+'), ('Manga and Anime', 'Manga and Anime'), ('Marxists', 'Marxists'), ('Mature Students Association', 'Mature Students Association'), ('GU Rock and Metal', 'GU Rock and Metal'), ('Music Club', 'Music Club'), ('Muslim Student Association', 'Muslim Student Association'), ('Opera', 'Opera'), ('Onekind', 'Onekind'), ('Philosophy', 'Philosophy'), ('Physics', 'Physics'), ('Plastic Surgery', 'Plastic Surgery'), ('Politics', 'Politics'), ('Quiz', 'Quiz'), ('Real Ale', 'Real Ale'), ('Robotics', 'Robotics'), ('Screenwriting', 'Screenwriting'), ('Sewing', 'Sewing'), ('Sexpression', 'Sexpression'), ('Shakespeare', 'Shakespeare'), ('Shrek', 'Shrek'), ('Sign Language', 'Sign Language'), ('Socialist', 'Socialist'), ('Society for Women in Tech', 'Society for Women in Tech'), ('Student Theatre at Glasgow', 'Student Theatre at Glasgow'), ('Successful Women at Glasgow', 'Successful Women at Glasgow'), ('Surgical', 'Surgical'), ('Sustainable Technologies', 'Sustainable Technologies'), ('Improv Teatime', 'Improv Teatime'), ('Tea', 'Tea'), ('Tech', 'Tech'), ('Tedx', 'Tedx'), ('Tennents Lager Appreciation', 'Tennents Lager Appreciation'), ('UGRacing', 'UGRacing'), ('Vegan', 'Vegan'), ('Walking', 'Walking'), ('Wine', 'Wine'), ('Women in Science, Tech, Engineering and Maths', 'Women in Science, Tech, Engineering and Maths'), ('Createive Writing', 'Createive Writing'), ('Hares and Hounds Running Club', 'Hares and Hounds Running Club'), ('Karate', 'Karate'), ('Hockey', 'Hockey'), ('Rugby Football', 'Rugby Football'), ('Sailing Club', 'Sailing Club'), ('Ski & Snowboard Club', 'Ski & Snowboard Club'), ('Aikido', 'Aikido'), ('American Football', 'American Football'), ('Athletics', 'Athletics'), ('Badminton', 'Badminton'), ('Basketball', 'Basketball'), ('Boat/Rowing', 'Boat/Rowing'), ('Boxing', 'Boxing'), ('Canoe', 'Canoe'), ('Cheerleading', 'Cheerleading'), ('Cricket', 'Cricket'), ('Curling', 'Curling'), ('Cycling', 'Cycling'), ('Fencing', 'Fencing'), ('Football', 'Football'), ('Gaelic Football', 'Gaelic Football'), ('Golf', 'Golf'), ('Gymnastics', 'Gymnastics'), ('Judo', 'Judo'), ('Kendo', 'Kendo'), ('Lacrosse', 'Lacrosse'), ('Mounteneering', 'Mounteneering'), ('Muay Thai Boxing', 'Muay Thai Boxing'), ('Netball', 'Netball'), ('Potholing (Caving)', 'Potholing (Caving)'), ('Riding/Equestrian', 'Riding/Equestrian'), ('Shinty', 'Shinty'), ('Shorinji Kempo', 'Shorinji Kempo'), ('Skydive', 'Skydive'), ('Squash', 'Squash'), ('Surf', 'Surf'), ('Swimming and Waterpolo', 'Swimming and Waterpolo'), ('Taekwondo', 'Taekwondo'), ('Trampoline', 'Trampoline'), ('Triathlon', 'Triathlon'), ('Ultimate Frisbee', 'Ultimate Frisbee'), ('Volleyball', 'Volleyball'), ('Wakeboarding', 'Wakeboarding'), ('Weightlifting', 'Weightlifting'), ('Yoga', 'Yoga'), ('Table Tennis', 'Table Tennis'), ('Tennis', 'Tennis')], max_length=50, unique=True),
        ),
    ]
