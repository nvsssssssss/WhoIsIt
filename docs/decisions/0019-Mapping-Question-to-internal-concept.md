# Question-to-Concept Mapping

Each user-facing question should map to exactly one internal concept
whenever possible.

The user-facing question is the natural-language representation,
while the internal concept is the normalized fact used by the
knowledge base and inference engine.

---

## Identity

| # | User-Facing Question | Internal Concept |
|---:|---|---|
| 1 | Is the character the main protagonist of their story? | `is_main_protagonist` |
| 2 | Is the character a protagonist? | `is_protagonist` |
| 3 | Is the character an antagonist? | `is_antagonist` |
| 4 | Is the character a supporting character? | `is_supporting_character` |
| 5 | Is the character's real identity different from their commonly known identity? | `has_alternate_identity` |
| 6 | Is the character a reincarnated person? | `is_reincarnated` |

---

## Media

| # | User-Facing Question | Internal Concept |
|---:|---|---|
| 7 | Is the character from an anime? | `appears_in_anime` |
| 8 | Is the character from a manga? | `appears_in_manga` |
| 9 | Is the character from a comic book? | `appears_in_comic` |
| 10 | Is the character from a movie? | `appears_in_movie` |
| 11 | Is the character from a television series? | `appears_in_tv_series` |
| 12 | Is the character from a web series? | `appears_in_web_series` |
| 13 | Is the character from a video game? | `appears_in_video_game` |
| 14 | Is the character from a novel? | `appears_in_novel` |
| 15 | Is the character from a light novel? | `appears_in_light_novel` |
| 16 | Did the character originate in a video game? | `originated_in_video_game` |
| 17 | Did the character originate in a comic or manga? | `originated_in_comic_or_manga` |
| 18 | Did the character originate in a novel or light novel? | `originated_in_novel_or_light_novel` |

---

## Universe

| # | User-Facing Question | Internal Concept |
|---:|---|---|
| 19 | Is the character from a Japanese fictional universe? | `universe_origin_japanese` |
| 20 | Is the character from a Western fictional universe? | `universe_origin_western` |
| 21 | Is the character from a superhero universe? | `universe_genre_superhero` |
| 22 | Is the character from a fantasy universe? | `universe_genre_fantasy` |
| 23 | Is the character from a science-fiction universe? | `universe_genre_scifi` |
| 24 | Is the character from a horror universe? | `universe_genre_horror` |
| 25 | Is the character from a school-based fictional universe? | `universe_setting_school` |
| 26 | Is the character from a universe involving magic? | `universe_contains_magic` |
| 27 | Is the character from a universe involving supernatural beings? | `universe_contains_supernatural_beings` |
| 28 | Is the character from a universe involving advanced technology? | `universe_contains_advanced_technology` |
| 29 | Is the character from a universe primarily set in the real world? | `universe_setting_real_world` |
| 30 | Is the character from a post-apocalyptic universe? | `universe_setting_post_apocalyptic` |
| 31 | Is the character from a dystopian universe? | `universe_setting_dystopian` |
| 32 | Is the character from a fictional universe based heavily on mythology? | `universe_based_on_mythology` |

---

## Role

| # | User-Facing Question | Internal Concept |
|---:|---|---|
| 33 | Is the character a hero? | `is_hero` |
| 34 | Is the character a villain? | `is_villain` |
| 35 | Is the character an antihero? | `is_antihero` |
| 36 | Is the character a mentor? | `is_mentor` |
| 37 | Is the character a leader? | `is_leader` |
| 38 | Is the character a student? | `is_student` |
| 39 | Is the character a teacher? | `is_teacher` |
| 40 | Is the character a warrior? | `is_warrior` |
| 41 | Is the character a soldier? | `is_soldier` |
| 42 | Is the character a detective? | `is_detective` |
| 43 | Is the character a ruler or monarch? | `is_ruler` |
| 44 | Is the character a member of an important organization? | `member_of_organization` |
| 45 | Is the character primarily an enemy of the protagonist? | `enemy_of_protagonist` |
| 46 | Is the character primarily an ally of the protagonist? | `ally_of_protagonist` |
| 47 | Is the character primarily comic relief? | `is_comic_relief` |

---

## Species

| # | User-Facing Question | Internal Concept |
|---:|---|---|
| 48 | Is the character human? | `species_human` |
| 49 | Is the character an animal? | `species_animal` |
| 50 | Is the character an alien? | `species_alien` |
| 51 | Is the character a robot? | `species_robot` |
| 52 | Is the character an artificial intelligence? | `species_ai` |
| 53 | Is the character a god or deity? | `species_deity` |
| 54 | Is the character a demon? | `species_demon` |
| 55 | Is the character a vampire? | `species_vampire` |
| 56 | Is the character a monster? | `species_monster` |
| 57 | Is the character a supernatural being? | `species_supernatural_being` |
| 58 | Is the character a spirit or ghost? | `species_spirit_or_ghost` |
| 59 | Is the character capable of transforming into another form? | `can_transform` |
| 60 | Is the character originally human? | `originally_human` |

---

## Abilities

| # | User-Facing Question | Internal Concept |
|---:|---|---|
| 61 | Does the character have supernatural abilities? | `has_supernatural_abilities` |
| 62 | Does the character have magical abilities? | `has_magic` |
| 63 | Does the character have superhuman strength? | `has_superhuman_strength` |
| 64 | Does the character have superhuman speed? | `has_superhuman_speed` |
| 65 | Can the character fly? | `can_fly` |
| 66 | Can the character teleport? | `can_teleport` |
| 67 | Can the character regenerate or heal rapidly? | `has_regeneration` |
| 68 | Can the character manipulate an element? | `can_manipulate_elements` |
| 69 | Can the character control fire? | `can_control_fire` |
| 70 | Can the character control water? | `can_control_water` |
| 71 | Can the character control electricity? | `can_control_electricity` |
| 72 | Can the character control ice? | `can_control_ice` |
| 73 | Can the character read minds? | `can_read_minds` |
| 74 | Can the character control other people's minds? | `can_control_minds` |
| 75 | Can the character see the future? | `can_see_future` |
| 76 | Can the character manipulate time? | `can_manipulate_time` |
| 77 | Can the character manipulate space? | `can_manipulate_space` |
| 78 | Can the character become invisible? | `can_become_invisible` |
| 79 | Can the character transform their body? | `can_transform_body` |
| 80 | Does the character use a special weapon as part of their abilities? | `uses_special_weapon` |
| 81 | Is the character highly skilled in martial arts? | `skilled_in_martial_arts` |
| 82 | Is the character highly intelligent? | `high_intelligence` |
| 83 | Is the character skilled at using technology? | `technology_proficiency` |

---

## Appearance

| # | User-Facing Question | Internal Concept |
|---:|---|---|
| 84 | Is the character male? | `gender_male` |
| 85 | Is the character female? | `gender_female` |
| 86 | Does the character have unusually colored hair? | `unusual_hair_color` |
| 87 | Does the character have long hair? | `has_long_hair` |
| 88 | Does the character have short hair? | `has_short_hair` |
| 89 | Does the character commonly wear a uniform? | `wears_uniform` |
| 90 | Does the character wear armor? | `wears_armor` |
| 91 | Does the character commonly wear a mask? | `wears_mask` |
| 92 | Does the character have a distinctive scar? | `has_scar` |
| 93 | Does the character have an unusual eye color? | `unusual_eye_color` |
| 94 | Does the character have non-human physical features? | `has_nonhuman_features` |
| 95 | Does the character have horns? | `has_horns` |
| 96 | Does the character have wings? | `has_wings` |
| 97 | Does the character carry a distinctive weapon? | `carries_distinctive_weapon` |
| 98 | Does the character's appearance change significantly during the story? | `appearance_changes` |

---

## Relationships

| # | User-Facing Question | Internal Concept |
|---:|---|---|
| 99 | Does the character have a brother? | `has_brother` |
| 100 | Does the character have a sister? | `has_sister` |
| 101 | Does the character have a child? | `has_child` |
| 102 | Does the character have a romantic partner? | `has_romantic_partner` |
| 103 | Does the character have a notable rival? | `has_rival` |
| 104 | Does the character have a mentor? | `has_mentor` |
| 105 | Is the character a mentor to another important character? | `mentors_character` |
| 106 | Is the character related to the protagonist? | `related_to_protagonist` |
| 107 | Is the character related to the main antagonist? | `related_to_main_antagonist` |
| 108 | Does the character belong to a team? | `member_of_team` |
| 109 | Does the character belong to an organization? | `member_of_organization` |
| 110 | Does the character have a teacher or master? | `has_teacher_or_master` |
| 111 | Does the character have a student or apprentice? | `has_student_or_apprentice` |
| 112 | Does the character have a significant enemy? | `has_enemy` |
| 113 | Does the character betray someone important to them? | `has_betrayed_someone` |
| 114 | Is the character responsible for protecting another character? | `protects_character` |
| 115 | Is the character seeking revenge against another character? | `seeking_revenge` |
| 116 | Does the character form an important alliance? | `forms_alliance` |
| 117 | Does the character become an ally after initially being an enemy? | `enemy_to_ally` |