from fastapi import (
    FastAPI,
    Response,
    status,
)

from app.schemas.company import (
    CompanyCreateModel,
    CompanyId,
    CompanyUpdateModel,
)
from app.schemas.user import (
    UserCreateModel,
    UserId,
    UserUpdateModel,
)
from app.schemas.vacancy import (
    VacancyCreateModel,
    VacancyId,
    VacancyUpdateModel,
)
from app.services.companies import service as companies_service
from app.services.users import service as users_service
from app.services.vacancies import service as vacancies_service

app = FastAPI()


@app.get("/v1/healthcheck")
def healthcheck_endpoint():
    return {"message": "up and running"}


@app.get("/v1/companies/{company_id}", status_code=status.HTTP_200_OK)
def get_company(company_id: CompanyId, response: Response):
    company = companies_service.get_company_by_company_id(company_id=company_id)
    if not company:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {
            "message": f"company={company_id} not found",
        }
    return {
        "message": company.dict(exclude_unset=True),
    }


@app.post("/v1/companies/", status_code=status.HTTP_201_CREATED)
def create_company(company_create: CompanyCreateModel, response: Response):
    company_created = companies_service.create_company(company_create=company_create)
    if not company_created:
        response.status_code = status.HTTP_409_CONFLICT
        return {
            "message": "company could not be created, email already exists",
        }
    return {
        "message": company_created.dict(exclude_unset=True),
    }


@app.patch("/v1/companies/{company_id}", status_code=status.HTTP_200_OK)
def update_company(company_id: CompanyId, company_update: CompanyUpdateModel, response: Response):
    company_updated = companies_service.update_company(company_id=company_id, company_update=company_update)
    if not company_updated:
        response.status_code = status.HTTP_409_CONFLICT
        return {
            "message": "company could not be updated",
        }
    return {
        "message": company_updated.dict(exclude_unset=True),
    }


@app.delete("/v1/companies/{company_id}", status_code=status.HTTP_200_OK)
def delete_company(company_id: CompanyId, response: Response):
    company_deleted = companies_service.delete_company_by_company_id(company_id=company_id)
    if not company_deleted:
        response.status_code = status.HTTP_409_CONFLICT
        return {
            "message": "unprocessable",
        }
    return {
        "message": company_deleted.dict(exclude_unset=True),
    }


@app.get("/v1/users/{user_id}", status_code=status.HTTP_200_OK)
def get_user(user_id: UserId, response: Response):
    user = users_service.get_user_by_user_id(user_id=user_id)
    if not user:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {
            "message": f"user={user_id} not found",
        }
    return {
        "message": user.dict(exclude_unset=True),
    }


@app.post("/v1/users/", status_code=status.HTTP_201_CREATED)
def create_user(user_create: UserCreateModel, response: Response):
    user_created = users_service.create_user(user_create=user_create)
    if not user_created:
        response.status_code = status.HTTP_409_CONFLICT
        return {
            "message": "user could not be created, email already exists",
        }
    return {
        "message": user_created.dict(exclude_unset=True),
    }


@app.patch("/v1/users/{user_id}", status_code=status.HTTP_200_OK)
def update_user(user_id: UserId, user_update: UserUpdateModel, response: Response):
    user_updated = users_service.update_user(user_id=user_id, user_update=user_update)
    if not user_updated:
        response.status_code = status.HTTP_409_CONFLICT
        return {
            "message": "user could not be updated",
        }
    return {
        "message": user_updated.dict(exclude_unset=True),
    }


@app.delete("/v1/users/{user_id}", status_code=status.HTTP_200_OK)
def delete_user(user_id: UserId, response: Response):
    user_deleted = users_service.delete_user_by_user_id(user_id=user_id)
    if not user_deleted:
        response.status_code = status.HTTP_409_CONFLICT
        return {
            "message": "unprocessable",
        }
    return {
        "message": user_deleted.dict(exclude_unset=True),
    }


@app.get("/v1/vacancies/{vacancy_id}", status_code=status.HTTP_200_OK)
def get_vacancy(vacancy_id: VacancyId, response: Response):
    vacancy = vacancies_service.get_vacancy_by_vacancy_id(vacancy_id=vacancy_id)
    if not vacancy:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {
            "message": f"vacancy={vacancy_id} not found",
        }
    return {
        "message": vacancy.dict(exclude_unset=True),
    }


@app.post("/v1/vacancies/", status_code=status.HTTP_201_CREATED)
def create_vacancy(vacancy_create: VacancyCreateModel, response: Response):
    vacancy_created = vacancies_service.create_vacancy(vacancy_create=vacancy_create)
    if not vacancy_created:
        response.status_code = status.HTTP_409_CONFLICT
        return {
            "message": "vacancy could not be created, email already exists",
        }
    return {
        "message": vacancy_created.dict(exclude_unset=True),
    }


@app.patch("/v1/vacancies/{vacancy_id}", status_code=status.HTTP_200_OK)
def update_vacancy(vacancy_id: VacancyId, vacancy_update: VacancyUpdateModel, response: Response):
    vacancy_updated = vacancies_service.update_vacancy(vacancy_id=vacancy_id, vacancy_update=vacancy_update)
    if not vacancy_updated:
        response.status_code = status.HTTP_409_CONFLICT
        return {
            "message": "vacancy could not be updated",
        }
    return {
        "message": vacancy_updated.dict(exclude_unset=True),
    }


@app.delete("/v1/vacancies/{vacancy_id}", status_code=status.HTTP_200_OK)
def delete_vacancy(vacancy_id: VacancyId, response: Response):
    vacancy_deleted = vacancies_service.delete_vacancy_by_vacancy_id(vacancy_id=vacancy_id)
    if not vacancy_deleted:
        response.status_code = status.HTTP_409_CONFLICT
        return {
            "message": "unprocessable",
        }
    return {
        "message": vacancy_deleted.dict(exclude_unset=True),
    }


@app.get("/v1/users/{user_id}/vacancies", status_code=status.HTTP_200_OK)
def get_user_vacancies_by_user_id(user_id: UserId, response: Response):
    vacancies = users_service.get_user_vacancies_by_user_id(user_id=user_id)
    if not vacancies:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {
            "message": f"no vacancies find for user={user_id}",
            "vacancies": [],
        }
    return {
        "message": f"{len(vacancies)} vacancies found for user={user_id}",
        "vacancies": [vacancy.dict(exclude_unset=True) for vacancy in vacancies],
    }
