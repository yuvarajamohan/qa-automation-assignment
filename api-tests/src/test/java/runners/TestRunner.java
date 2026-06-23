package runners;

import com.intuit.karate.junit5.Karate;

class TestRunner {

    @Karate.Test
    Karate testAll() {
        return Karate.run(
                "classpath:features/01_weather_refusal.feature",
                "classpath:features/02_remote_work.feature",
                "classpath:features/03_americas_meal.feature",
                "classpath:features/04_emea_meal.feature",
                "classpath:features/05_apac_refusal.feature",
                "classpath:features/06_engineering.feature",
                "classpath:features/07_employee_denied.feature",
                "classpath:features/08_procurement.feature",
                "classpath:features/09_draft_policy.feature",
                "classpath:features/10_prompt_injection.feature"
        );
    }
}