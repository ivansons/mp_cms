var mp;
if (!mp) {
    mp = {};
}

var mp_phone;

var EU = [
    "AL", /* Albania */
    "AD", /* Andorra */
    "AM", /* Armenia */
    "AT", /* Austria */
    "BY", /* Belarus */
    "BE", /* Belgium */
    "BA", /* Bosnia and Herzegovina */
    "BG", /* Bulgaria */
    "CH", /* Switzerland */
    "CY", /* Cyprus */
    "CZ", /* Czech Republic */
    "DE", /* Germany */
    "DK", /* Denmark */
    "EE", /* Estonia */
    "ES", /* Spain */
    "FO", /* Faeroe Islands */
    "FI", /* Finland */
    "FR", /* France */
    "GB", /* United Kingdom */
    "GE", /* Georgia */
    "GI", /* Gibraltar */
    "GR", /* Greece */
    "HU", /* Hungary */
    "HR", /* Croatia */
    "IE", /* Ireland */
    "IS", /* Iceland */
    "IT", /* Italy */
    "LT", /* Lithuania */
    "LU", /* Luxembourg */
    "LV", /* Latvia */
    "MC", /* Monaco */
    "MK", /* Macedonia */
    "MT", /* Malta */
    "NO", /* Norway */
    "NL", /* Netherlands */
    "PO", /* Poland */
    "PT", /* Portugal */
    "RO", /* Romania */
    "RU", /* Russian Federation */
    "SE", /* Sweden */
    "SI", /* Slovenia */
    "SK", /* Slovakia */
    "SM", /* San Marino */
    "TR", /* Turkey */
    "UA", /* Ukraine */
    "VA" /* Vatican City State */
];

mp.geoip = {
    settings: {
        "geoip": {
            'url': 'https://static.matterport.com/geoip/',
            'field_name': 'country_code'
        }
    },

    get_country: function () {
        return mp.geoip.request_country_code(mp.geoip.settings.geoip);
    },

    request_country_code: function (provider) {
        jQuery.ajax({
            url: provider.url,
            success: function (response) {
                var country_code = JSON.parse(response).country_code;
                mp_phone = mp.geoip.utils.get_object_to_present(country_code);
                mp.geoip.set_phone_number();
            }
        });
    },
    set_phone_number: function () {
        if (mp_phone) {
            $(".geo-phone-number-text").text(mp_phone.text);
            $(".geo-phone-number-link").attr("href", "tel:" + mp_phone.link);
        }
    }
};

var phoneNumbers = {
    'US': {
        text: '888-993-8990',
        link: '+18889938990'
    },
    'US_AEC': {
        text: '888-628-8018',
        link: '+18886288018'
    },
    'CA': {
        text: '437-800-5701',
        link: '+14378005701'
    },
    'MX': {
        text: '+55 55 85266215',
        link: '+555585266215'
    },
    'UK': {
        text: '+44 (0) 20 3874 7580',
        link: '+4402038747580'
    },
    'FR': {
        text: '+33 1 85650810',
        link: '+33185650810'
    },
    'ES': {
        text: '+34 910 482834',
        link: '+34910482834'
    },
    'DE': {
        text: '+49 6956 608908',
        link: '+496956608908'
    },
    'IT': {
        text: '+39 0287045024',
        link: '+390287045024'
    },
    'JP': {
        text: '+81 03-4540-8486',
        link: '+810345408486'
    },
    'AU': {
        text: '+61 2 40444598',
        link: '+61240444598'
    }
}

mp.geoip.utils = {
    get_object_to_present: function (country_code) {
        if (country_code === 'US' && $.inArray(window.location.pathname, [
            '/3d-scanning-construction-engineering/',
            '/3d-scanning-for-as-built-modeling/',
            '/3d-building-information-modeling/',
            '/3d-construction-documentation/',
            '/3d-scanning-pricing/',
            '/engineering-contact-us/'
        ]) !== -1) {
            return phoneNumbers.US_AEC;
        }
        var phoneNumber = phoneNumbers[country_code];
        if (phoneNumber) {
            return phoneNumber;
        }
        if (EU.indexOf(country_code) != -1) {
            return {
                text: '+44 (0) 20 3874 7580',
                link: '+4402038747580'
            }
        }
        return phoneNumbers.US;
    },
    get_phone_number: function () {
        mp.geoip.get_country();
    }
};

mp.geoip.utils.get_phone_number();
