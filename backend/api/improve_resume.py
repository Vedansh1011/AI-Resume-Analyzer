from fastapi import APIRouter, HTTPException

from services.resume_improver import improve_resume


router = APIRouter()


@router.post("/improve-resume")
def improve_resume_endpoint(resume_data: dict):

    try:
        result = improve_resume(resume_data)

        return {
            "success": True,
            "improvement": result
        }

    except Exception as e:

        error_message = str(e)

        if "429" in error_message or "RESOURCE_EXHAUSTED" in error_message:
            raise HTTPException(
                status_code=429,
                detail=(
                    "Gemini API quota has been exceeded. "
                    "Please try again after the quota resets."
                )
            )

        if (
            "temporarily unavailable" in error_message.lower()
            or "503" in error_message
        ):
            raise HTTPException(
                status_code=503,
                detail=(
                    "The AI service is temporarily unavailable. "
                    "Please try again in a few moments."
                )
            )

        raise HTTPException(
            status_code=500,
            detail="Unable to generate resume improvements."
        )
