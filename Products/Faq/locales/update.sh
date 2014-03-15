# call ./locales/update.sh
domain=faq
i18ndude rebuild-pot --pot locales/$domain.pot --create $domain ./
i18ndude sync --pot locales/$domain.pot locales/*/LC_MESSAGES/$domain.po
