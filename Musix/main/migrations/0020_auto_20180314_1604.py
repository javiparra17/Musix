# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-14 15:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0019_song_finished'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='infouser',
            name='infoactor_ptr',
        ),
        migrations.RemoveField(
            model_name='infouser',
            name='user',
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('actor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.Actor')),
                ('registrationDate', models.DateField(auto_now_add=True)),
                ('gender', models.CharField(choices=[(b'M', b'Male'), (b'F', b'Female'), (b'O', b'Other')], max_length=7)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('country', models.CharField(choices=[(b'AF', b'Afganist\xc3\xa1n'), (b'AL', b'Albania'), (b'DE', b'Alemania'), (b'AD', b'Andorra'), (b'AO', b'Angola'), (b'AI', b'Anguilla'), (b'AQ', b'Ant\xc3\xa1rtida'), (b'AG', b'Antigua y Barbuda'), (b'AN', b'Antillas Holandesas'), (b'SA', b'Arabia Saud\xc3\xad'), (b'DZ', b'Argelia'), (b'AR', b'Argentina'), (b'AM', b'Armenia'), (b'AW', b'Aruba'), (b'AU', b'Australia'), (b'AT', b'Austria'), (b'AZ', b'Azerbaiy\xc3\xa1n'), (b'BS', b'Bahamas'), (b'BH', b'Bahrein'), (b'BD', b'Bangladesh'), (b'BB', b'Barbados'), (b'BE', b'B\xc3\xa9lgica'), (b'BZ', b'Belice'), (b'BJ', b'Benin'), (b'BM', b'Bermudas'), (b'BY', b'Bielorrusia'), (b'MM', b'Birmania'), (b'BO', b'Bolivia'), (b'BA', b'Bosnia y Herzegovina'), (b'BW', b'Botswana'), (b'BR', b'Brasil'), (b'BN', b'Brunei'), (b'BG', b'Bulgaria'), (b'BF', b'Burkina Faso'), (b'BI', b'Burundi'), (b'BT', b'But\xc3\xa1n'), (b'CV', b'Cabo Verde'), (b'KH', b'Camboya'), (b'CM', b'Camer\xc3\xban'), (b'CA', b'Canad\xc3\xa1'), (b'TD', b'Chad'), (b'CL', b'Chile'), (b'CN', b'China'), (b'CY', b'Chipre'), (b'VA', b'Ciudad del Vaticano (Santa Sede)'), (b'CO', b'Colombia'), (b'KM', b'Comores'), (b'CG', b'Congo'), (b'CD', b'Congo, Rep\xc3\xbablica Democr\xc3\xa1tica del'), (b'KR', b'Corea'), (b'KP', b'Corea del Norte'), (b'CI', b'Costa de Marfil'), (b'CR', b'Costa Rica'), (b'HR', b'Croacia'), (b'CU', b'Cuba'), (b'DK', b'Dinamarca'), (b'DJ', b'Djibouti'), (b'DM', b'Dominica'), (b'EC', b'Ecuador'), (b'EG', b'Egipto'), (b'SV', b'El Salvador'), (b'AE', b'Emiratos \xc3\x81rabes Unidos'), (b'ER', b'Eritrea'), (b'SI', b'Eslovenia'), (b'ES', b'Espa\xc3\xb1a'), (b'US', b'Estados Unidos'), (b'EE', b'Estonia'), (b'ET', b'Etiop\xc3\xada'), (b'FJ', b'Fiji'), (b'PH', b'Filipinas'), (b'FI', b'Finlandia'), (b'FR', b'Francia'), (b'GA', b'Gab\xc3\xb3n'), (b'GM', b'Gambia'), (b'GE', b'Georgia'), (b'GH', b'Ghana'), (b'GI', b'Gibraltar'), (b'GD', b'Granada'), (b'GR', b'Grecia'), (b'GL', b'Groenlandia'), (b'GP', b'Guadalupe'), (b'GU', b'Guam'), (b'GT', b'Guatemala'), (b'GY', b'Guayana'), (b'GF', b'Guayana Francesa'), (b'GN', b'Guinea'), (b'GQ', b'Guinea Ecuatorial'), (b'GW', b'Guinea-Bissau'), (b'HT', b'Hait\xc3\xad'), (b'HN', b'Honduras'), (b'HU', b'Hungr\xc3\xada'), (b'IN', b'India'), (b'ID', b'Indonesia'), (b'IQ', b'Irak'), (b'IR', b'Ir\xc3\xa1n'), (b'IE', b'Irlanda'), (b'BV', b'Isla Bouvet'), (b'CX', b'Isla de Christmas'), (b'IS', b'Islandia'), (b'KY', b'Islas Caim\xc3\xa1n'), (b'CK', b'Islas Cook'), (b'CC', b'Islas de Coco'), (b'FO', b'Islas Faroe'), (b'HM', b'Islas Heard y McDonald'), (b'FK', b'Islas Malvinas'), (b'MP', b'Islas Marianas del Norte'), (b'MH', b'Islas Marshall'), (b'UM', b'Islas menores de Estados Unidos'), (b'PW', b'Islas Palau'), (b'SB', b'Islas Salom\xc3\xb3n'), (b'SJ', b'Islas Svalbard y Jan Mayen'), (b'TK', b'Islas Tokelau'), (b'TC', b'Islas Turks y Caicos'), (b'VI', b'Islas V\xc3\xadrgenes (EEUU)'), (b'VG', b'Islas V\xc3\xadrgenes (Reino Unido)'), (b'WF', b'Islas Wallis y Futuna'), (b'IL', b'Israel'), (b'IT', b'Italia'), (b'JM', b'Jamaica'), (b'JP', b'Jap\xc3\xb3n'), (b'JO', b'Jordania'), (b'KZ', b'Kazajist\xc3\xa1n'), (b'KE', b'Kenia'), (b'KG', b'Kirguizist\xc3\xa1n'), (b'KI', b'Kiribati'), (b'KW', b'Kuwait'), (b'LA', b'Laos'), (b'LS', b'Lesotho'), (b'LV', b'Letonia'), (b'LB', b'L\xc3\xadbano'), (b'LR', b'Liberia'), (b'LY', b'Libia'), (b'LI', b'Liechtenstein'), (b'LT', b'Lituania'), (b'LU', b'Luxemburgo'), (b'MK', b'Macedonia, Ex-Rep\xc3\xbablica Yugoslava de'), (b'MG', b'Madagascar'), (b'MY', b'Malasia'), (b'MW', b'Malawi'), (b'MV', b'Maldivas'), (b'ML', b'Mal\xc3\xad'), (b'MT', b'Malta'), (b'MA', b'Marruecos'), (b'MQ', b'Martinica'), (b'MU', b'Mauricio'), (b'MR', b'Mauritania'), (b'YT', b'Mayotte'), (b'MX', b'M\xc3\xa9xico'), (b'FM', b'Micronesia'), (b'MD', b'Moldavia'), (b'MC', b'M\xc3\xb3naco'), (b'MN', b'Mongolia'), (b'MS', b'Montserrat'), (b'MZ', b'Mozambique'), (b'NA', b'Namibia'), (b'NR', b'Nauru'), (b'NP', b'Nepal'), (b'NI', b'Nicaragua'), (b'NE', b'N\xc3\xadger'), (b'NG', b'Nigeria'), (b'NU', b'Niue'), (b'NF', b'Norfolk'), (b'NO', b'Noruega'), (b'NC', b'Nueva Caledonia'), (b'NZ', b'Nueva Zelanda'), (b'OM', b'Oman'), (b'NL', b'Pa\xc3\xadses Bajos'), (b'PA', b'Panam\xc3\xa1'), (b'PG', b'Pap\xc3\xbaa Nueva Guinea'), (b'PK', b'Paquist\xc3\xa1n'), (b'PY', b'Paraguay'), (b'PE', b'Per\xc3\xba'), (b'PN', b'Pitcairn'), (b'PF', b'Polinesia Francesa'), (b'PL', b'Polonia'), (b'PT', b'Portugal'), (b'PR', b'Puerto Rico'), (b'QA', b'Qatar'), (b'UK', b'Reino Unido'), (b'CF', b'Rep\xc3\xbablica Centroafricana'), (b'CZ', b'Rep\xc3\xbablica Checa'), (b'ZA', b'Rep\xc3\xbablica de Sud\xc3\xa1frica'), (b'DO', b'Rep\xc3\xbablica Dominicana'), (b'SK', b'Rep\xc3\xbablica Eslovaca'), (b'RE', b'Reuni\xc3\xb3n'), (b'RW', b'Ruanda'), (b'RO', b'Rumania'), (b'RU', b'Rusia'), (b'EH', b'S\xc3\xa1hara Occidental'), (b'KN', b'Saint Kitts y Nevis'), (b'WS', b'Samoa'), (b'AS', b'Samoa Americana'), (b'SM', b'San Marino'), (b'VC', b'San Vicente y Granadinas'), (b'SH', b'Santa Helena'), (b'LC', b'Santa Luc\xc3\xada'), (b'ST', b'Santo Tom\xc3\xa9 y Pr\xc3\xadncipe'), (b'SN', b'Senegal'), (b'SC', b'Seychelles'), (b'SL', b'Sierra Leona'), (b'SG', b'Singapur'), (b'SY', b'Siria'), (b'SO', b'Somalia'), (b'LK', b'Sri Lanka'), (b'PM', b'St Pierre y Miquelon'), (b'SZ', b'Suazilandia'), (b'SD', b'Sud\xc3\xa1n'), (b'SE', b'Suecia'), (b'CH', b'Suiza'), (b'SR', b'Surinam'), (b'TH', b'Tailandia'), (b'TW', b'Taiw\xc3\xa1n'), (b'TZ', b'Tanzania'), (b'TJ', b'Tayikist\xc3\xa1n'), (b'TF', b'Territorios franceses del Sur'), (b'TP', b'Timor Oriental'), (b'TG', b'Togo'), (b'TO', b'Tonga'), (b'TT', b'Trinidad y Tobago'), (b'TN', b'T\xc3\xbanez'), (b'TM', b'Turkmenist\xc3\xa1n'), (b'TR', b'Turqu\xc3\xada'), (b'TV', b'Tuvalu'), (b'UA', b'Ucrania'), (b'UG', b'Uganda'), (b'UY', b'Uruguay'), (b'UZ', b'Uzbekist\xc3\xa1n'), (b'VU', b'Vanuatu'), (b'VE', b'Venezuela'), (b'VN', b'Vietnam'), (b'YE', b'Yemen'), (b'YU', b'Yugoslavia'), (b'ZM', b'Zambia'), (b'ZW', b'Zimbabue')], max_length=100)),
                ('photo', models.ImageField(null=True, upload_to=b'')),
                ('city', models.CharField(blank=True, max_length=50)),
                ('premium', models.BooleanField(default=False)),
            ],
            bases=('main.actor',),
        ),
        migrations.DeleteModel(
            name='InfoActor',
        ),
        migrations.DeleteModel(
            name='InfoUser',
        ),
        migrations.AddField(
            model_name='actor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='song',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.Person'),
        ),
    ]
