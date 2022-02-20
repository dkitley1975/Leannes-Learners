from django.test import SimpleTestCase
from django.urls import reverse, resolve
from leannes_learners_data.views import AboutUsPage, ContactUsPage, ContactSuccessView, PassPlusPage, PricesPage, TermsPage, Testimonials, TemplateView


class TestLeannesLearnersDataUrls(SimpleTestCase):
    """ Test the URLS """

    def test_home_url_resolves(self):
        """
        Test that the url for the Home Page is correct.
        """
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, Testimonials)

    def test_about_Us_url_resolves(self):
        """
        Test the about us url.
        """
        url = reverse('about-us')
        self.assertEquals(resolve(url).func.view_class, AboutUsPage)

    def test_contact_us_url_resolves(self):
        """ Test the Contact Us Page URL is correct """
        url = reverse('contact-us')
        self.assertEquals(resolve(url).func.view_class, ContactUsPage)

    def test_pass_plus_page_url_resolves(self):
        """ Test the Pass Plus Page URL is correct """
        url = reverse('pass-plus')
        self.assertEquals(resolve(url).func.view_class, PassPlusPage)

    def test_prices_page_url_resolves(self):
        """ Test the Prices Page URL is correct """
        url = reverse('prices')
        self.assertEquals(resolve(url).func.view_class, PricesPage)

    def test_contact_success_page_url_resolves(self):
        """ Test the Successful Contact Page URL is correct """
        url = reverse('success')
        self.assertEquals(resolve(url).func.view_class, ContactSuccessView)

    def test_ts_and_cs_page_url_resolves(self):
        """ Test the Terms and Conditions Page URL is correct """
        url = reverse('terms-and-conditions')
        self.assertEquals(resolve(url).func.view_class, TermsPage)

    def test_traffic_map_Page_url_resolves(self):
        """ Test the traffic map Page URL is correct """
        url = reverse('local-traffic')
        self.assertEquals(resolve(url).func.view_class, TemplateView)
        